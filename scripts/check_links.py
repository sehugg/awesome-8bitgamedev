#!/usr/bin/env python3
"""Check links in markdown files and suggest Wayback Machine snapshots for dead ones.

Usage: ./check_links.py [-j N] [-t SECONDS] [--all-failures] [--suggest-https] [FILE ...]
Defaults to README.md. Exits 1 if any dead links are found.
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (compatible; awesome-8bitgamedev-linkcheck/1.0)"
URL_RE = re.compile(r"https?://[^\s)>\]\"'<]+")
DEAD_CODES = {404, 410}


def extract(files):
    """Return {url: [(file, lineno), ...]}."""
    found = {}
    for path in files:
        with open(path, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                for url in URL_RE.findall(line):
                    url = url.rstrip(".,;:")
                    found.setdefault(url, []).append((path, n))
    return found


def fetch(url, method, timeout):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status


def check(url, timeout):
    """Return (status, error). status is an HTTP code or None on network error."""
    # Some servers reject HEAD, so retry with GET on any HTTP error.
    for method in ("HEAD", "GET"):
        try:
            return fetch(url, method, timeout), None
        except urllib.error.HTTPError as e:
            if method == "GET":
                return e.code, None
        except Exception as e:  # DNS failure, timeout, TLS error...
            if method == "GET":
                return None, str(getattr(e, "reason", e))
    return None, "unknown"


def _get(api, timeout, retries=3):
    """GET with backoff; archive.org rate-limits (429) aggressively."""
    for i in range(retries):
        try:
            req = urllib.request.Request(api, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                return None
        except Exception:
            return None
        time.sleep(2 ** (i + 1))
    return None


def wayback(url, timeout):
    """Return the most recent archived snapshot URL, or None."""
    quoted = urllib.parse.quote(url, safe="")
    # CDX is more reliable than the availability API, which often returns nothing
    body = _get("https://web.archive.org/cdx/search/cdx?output=json&limit=-1"
                "&filter=statuscode:200&fl=timestamp,original&url=" + quoted, timeout)
    try:
        rows = json.loads(body) if body else []
        if len(rows) > 1:
            ts, orig = rows[-1]
            return f"https://web.archive.org/web/{ts}/{orig}"
    except ValueError:
        pass
    body = _get("https://archive.org/wayback/available?url=" + quoted, timeout)
    try:
        snap = json.loads(body).get("archived_snapshots", {}).get("closest") if body else None
        if snap and snap.get("available"):
            return snap["url"]
    except ValueError:
        pass
    return None


def process(url, timeout, all_failures, suggest_https=False):
    status, err = check(url, timeout)
    if status is not None and status < 400:
        if suggest_https and url.startswith("http://"):
            secure = "https://" + url[len("http://"):]
            s2, _ = check(secure, timeout)
            if s2 is not None and s2 < 400:
                return url, "https", status, None, secure
        return url, "ok", status, None, None
    dead = status in DEAD_CODES or (all_failures and (status is None or status >= 400))
    if dead:
        return url, "dead", status, err, wayback(url, timeout)
    # Network-level failures (DNS, refused, timeout) usually mean the site is gone,
    # so look for an archive copy. 403/429/5xx are often bot-blocking: no lookup.
    return url, "warn", status, err, wayback(url, timeout) if status is None else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*", default=["README.md"])
    ap.add_argument("-j", "--jobs", type=int, default=16)
    ap.add_argument("-t", "--timeout", type=float, default=15)
    ap.add_argument("--all-failures", action="store_true",
                    help="treat any failure (not just 404/410) as dead and look up archives")
    ap.add_argument("--suggest-https", action="store_true",
                    help="for working http:// links, report ones that also work over https://")
    args = ap.parse_args()

    urls = extract(args.files)
    print(f"Checking {len(urls)} unique links...", file=sys.stderr)
    with ThreadPoolExecutor(args.jobs) as ex:
        results = list(ex.map(lambda u: process(u, args.timeout, args.all_failures, args.suggest_https), urls))

    dead = [r for r in results if r[1] == "dead"]
    warn = [r for r in results if r[1] == "warn"]
    for url, _, status, err, snap in dead:
        print(f"DEAD  [{status or err}] {url}")
        for path, n in urls[url]:
            print(f"        at {path}:{n}")
        print(f"        wayback: {snap or 'no snapshot found'}")
    for url, kind, _, _, secure in results:
        if kind == "https":
            print(f"HTTPS {url}\n        -> {secure}")
    for url, _, status, err, snap in warn:
        print(f"WARN  [{status or err}] {url} (possibly transient or bot-blocked)")
        if status is None:
            print(f"        wayback: {snap or 'no snapshot found'}")
    print(f"\n{sum(r[1] in ("ok", "https") for r in results)} ok, {len(warn)} warnings, {len(dead)} dead",
          file=sys.stderr)
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
