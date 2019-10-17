# Awesome 8-bit Game Dev

A curated list of awesome resources for 8-bit retro game development, brought to you by [8bitworkshop](https://8bitworkshop.com/).

## Table of Contents

- [Home Consoles](#home-consoles)
  - [Fairchild Channel F](#fairchild-channel-f)
  - [Bally Astrocade](#ball-yastrocade)
  - [Atari 2600](#atari-2600)
  - [APF MP-1000](#apf-mp-1000)
  - [Magnavox Odyssey²](#Magnavox-Odyssey²)
  - [Intellivision](#intellivision)
  - [ColecoVision](#colecovision)
  - [Vectrex](#vectrex)
  - [NES](#nes)
  - [Atari 7800](#atari-7800)
  - [Sega Master System](#sega-master-system)
- [Home Computers](#home-computers)
  - [Apple I](#apple-i)
  - [Commodore PET](#commodore-pet)
  - [Compucolor](#compucolor)
  - [TRS-80](#trs-80)
  - [Apple II/II+/IIe](#apple-ii)
  - [Atari 400/600/800/XL/XE](#atari-8-bit)
  - [TI 99/4](#ti-99-4)
  - [Commodore VIC-20](#commodore-vic-20)
  - [Acorn Atom/BBC Micro]
  - [Sinclair ZX80/ZX81/ZX Spectrum]
  - [Commodore 64](#commodore-64)
  - [MSX](#msx)
- [Arcade Games](#arcade-games)
- [Hardware Design](#hardware-design)
- [CPUs](#cpus)
  - [6502](#6502)
  - [Z80](#z80)
- [Programming Tools](#programming-tools)
  - [Assemblers](#assemblers)
  - [Compilers](#compilers)
- [Contributing](#contributing)

## Home Consoles

### Fairchild Channel F

* [VES Wiki](http://channelf.se/veswiki/index.php?title=Main_Page) and [tutorial](http://channelf.se/veswiki/index.php?title=Tutorial:Beginner%27s_Guide_to_the_Channel_F)

* [Sean Riddle's Channel F Info](http://seanriddle.com/chanfinfo.html) including a homebrew Tetris clone

* [Fairchild F8 Info](http://www.nyx.net/~lturner/public_html/Fairchild_F8.html) and [instruction set](http://www.nyx.net/~lturner/public_html/F8_ins.html)

### Bally Astrocade

* [Bally Alley](https://ballyalley.com/) - An archive of all things Bally Astrocade.

* [The Better Bally Book](http://metopal.com/projects/ballybook/doku.php) - A wiki dedicated to organizing, annotating, and improving Software and Hardware for the Bally Arcade, a technical manual for the Bally Home Computer/Arcade/Astrocade originally published in 1978 by Dave Nutting Associates. 

* [hxlnt's Astrocade Dev](https://github.com/hxlnt/astrocade) - Z80 demos and graphics tools for the Astrocade. Also see this [thread](https://atariage.com/forums/topic/251416-programming-the-bally-arcadeastrocade/).

### Atari 2600

* [Stella Programmer's Guide](https://alienbill.com/2600/101/docs/stella.html) - The official guide to programming the Atari 2600, from Atari employee Steve Wright. 

* [Atari 2600 Advanced Programming Guide](http://www.qotile.net/minidig/docs/2600_advanced_prog_guide.txt) - Paul Slocum compiled this list of Atari 2600 programming techniques, including an HMOVE timing chart.  Also see this [list of tricks](http://www.qotile.net/minidig/tricks.html).

* [TIA Hardware Notes](http://www.atarihq.com/danb/files/TIA_HW_Notes.txt) - A detailed analysis of the TIA chip by Andrew Towers.

* [Kirk Israel's 2600 Programming Page](https://alienbill.com/2600/) - A bunch of links by a 2600 homebrew developer. Also see his [2600 Cookbook](http://alienbill.com/2600/cookbook/).

* [Random Terrain 2600 Page](https://www.randomterrain.com/atari-2600-memories.html) - Includes [Atari 2600 Programming for Newbies](https://www.randomterrain.com/atari-2600-memories-tutorial-andrew-davie-01.html), batariBasic info, programming tools, and much more.

* [BJARS Atari Archives](http://www.bjars.com/) - Steve Engelhardt's site full of homebrew, hacks, online tools, references, and disassembled code.

### AFP MP-1000

* [AFP MP-1000 Programming](https://orphanedgames.com/APF/index.html) - AFP/6800 programming tools for Windows, and documentation.

### ColecoVision

* [ColecoVision Tech Info](http://www.atarihq.com/danb/files/CV-Tech.txt) and [Sound Info(http://www.atarihq.com/danb/files/CV-Sound.txt).

* Philipp Klaus Krause's [tutorial](http://www.colecovision.eu/ColecoVision/development/tutorial1.shtml) on using [libCV](http://www.colecovision.eu/ColecoVision/development/libcv.shtml) to develop games in C using SDCC. Also includes graphics conversion and compression tools.

* [Texas Instruments TMS9918A VDP](http://bifi.msxnet.org/msxnet//tech/tms9918a.txt) info by Sean Young. Also see [here](http://www.unige.ch/medecine/nouspikel/ti99/tms9918a.htm).

* [ColecoVision.dk](http://www.colecovision.dk/tools.htm) - Tools and homebrew source code.

* [Convert9918](https://github.com/tursilion/convert9918) - (Windows) This program can convert most modern graphics into a form compatible with the TMS9918A bitmap mode.

### Sega SG-1000

* [Sega Game 1000 Specifications](http://www.smspower.org/uploads/Development/sg1000.txt) - by Omar Cornut / Zoop

### NES

* [NesDev Wiki](http://wiki.nesdev.com/w/index.php/Nesdev_Wiki) - Comprehensive site with NES programming tutorials, reference guides, and homebrew.

* [Shiru's Stuff](https://shiru.untergrund.net/software.shtml) - Shiru has lots of NES programming tools, and the article [programming NES games in C](https://shiru.untergrund.net/articles/programming_nes_games_in_c.htm).

* [Dustmop's NES Graphics](http://www.dustmop.io/blog/2015/04/28/nes-graphics-part-1/) - Describes NES graphics in detail.

* [nesdoug](https://nesdoug.com/) - Step-by-step tutorial on making a NES game in C.

* [Lizard NES](http://lizardnes.com/) - Homebrew game with a great development blog.

* [Mega Cat Studios](https://megacatstudios.com/blogs/press/tagged/nes-graphics) - Some good blog posts about efficiently managing NES graphics assets.

### Atari 7800

* [Atari 7800 (Dan Boris)](https://atarihq.com/danb/a7800.shtml) - System Specs, Cartridge Information, Links, The 'Encryption' Issue, Technical Files, and more.

* [Atari 7800 Software Guide](http://7800.8bitdev.org/index.php/7800_Software_Guide) - 7800 hardware description, registers, DMA timing, and more.

* [Atari 7800 Programming Wiki](https://sites.google.com/site/atari7800wiki/) - This site is intended to be a reference for the Atari 7800 Programming mailing list, with information culled from the mailing list archives and other sources (i.e. Atari Age forums)

### Sega Master System

* [SMS Power](http://www.smspower.org/Development/Index) - This area is dedicated to studying, programming, hacking of Sega 8-bit hardware and software.
[Technical info](http://www.smspower.org/uploads/Development/richard.txt), 
[VDP info](http://www.smspower.org/uploads/Development/msvdp-20021112.txt),
[SN76489 sound chip info](http://www.smspower.org/uploads/Development/SN76489-20030421.txt)

## Home Computers

### Apple I

* [Understanding the Apple I](https://www.applefritter.com/replica/chapter7)

* Signetics [2513](https://www.applefritter.com/files/signetics2513.pdf), [2504](http://retro.hansotten.nl/uploads/6502docs/signetics2504.pdf), and [2519](http://retro.hansotten.nl/uploads/6502docs/signetics2519.pdf) datasheets

### Commodore PET

### Compucolor

### TRS-80

### Apple II

### Atari 8-bit

* [ANTIC, GTIA and timing info](https://www.atarimax.com/jindroush.atari.org/atanttim.html)

* [Reverse engineering Atari 8-bit video](http://www.virtualdub.org/blog/pivot/entry.php?id=243)

* [ANTIC Timings](http://www.beipmu.com/Antic_Timings.txt)

* [ANTIC Registers](https://user.xmission.com/~trevin/atari/antic_regs.html) and [Instructions](https://user.xmission.com/~trevin/atari/antic_insns.html); [GTIA Registers](https://user.xmission.com/~trevin/atari/gtia_regs.html)

* [TRANSPORTING ATARI COMPUTER PROGRAMS TO THE ATARI 5200](http://www.atarimuseum.com/videogames/consoles/5200/conv_to_5200.html) - A.N.A.L.O.G. #15, January 1984

* [Atari Cartridge Images](https://github.com/dmlloyd/atari800/blob/master/DOC/cart.txt)

* [Atari 5200 Memory Map](http://atariage.com/forums/topic/169971-5200-memory-map/)

### TI 99/4

### Commodore VIC-20

### Acorn Atom/BBC Micro

### Sinclair ZX80/ZX81/ZX Spectrum

### Commodore 64

* [C64 Wiki](https://www.c64-wiki.com/wiki/C64)

* [C64 Programmer's Reference Guide](http://www.zimmers.net/cbmpics/cbm/c64/c64prg.txt)

* [The MOS 6567/6569 video controller (VIC-II)](http://www.zimmers.net/cbmpics/cbm/c64/vic-ii.txt)

* [C64 Memory Map](http://sta.c64.org/cbm64mem.html)

* [accurately reproducing the Video Output of a Commodore C64](http://hitmen.c02.at/temp/palstuff/)

* [The CIA 6526](https://www.c64-wiki.com/wiki/CIA)

* [Reading the C64 Keyboard](https://codebase64.org/doku.php?id=base:reading_the_keyboard) and [How the C64 Keyboard Works](http://www.c64os.com/post/?p=45)

### MSX

* [MSX Wiki](https://www.msx.org/wiki/)

* [MSX Assembly Page](http://map.grauw.nl/)

* [Konamiman's MSX page](https://www.konamiman.com/msx/msx-e.html)

* [The MSX Red Book](https://github.com/gseidler/The-MSX-Red-Book/blob/master/the_msx_red_book.md) - The aim of this book is to provide a description of the standard MSX hardware and software at a level of detail sufficient to satisfy that most demanding of users, the machine code programmer.

* [VDP Programming Tutorial](http://map.grauw.nl/articles/vdp_tut.php) - Examples of programming the TMS9918A/v9938/v9958 from Z80 assembly language.

## Arcade Games

* [Computer Archeology](http://www.computerarcheology.com/Arcade/) - Investigating Asteroids, Crazy Climber, Defender, Frogger (Sound), Galaga, Moon Patrol, Omega Race, Space Invaders, Time Pilot (Sound) and the [Asteroids Digital Vector Generator](http://www.computerarcheology.com/Arcade/Asteroids/DVG.html)

* [Programming the Atari XY Vector Generator](http://arcarc.xmission.com/Tech/neilw_xy.txt)

* Jed Margolin's [The Secret Life of Vector Generators](https://www.jmargolin.com/vgens/vgens.htm) and [The Secret Life of XY Monitors](https://www.jmargolin.com/xy/xymon.htm)

* [Sean Riddle's Williams Game Hardware Info](http://seanriddle.com/willhard.html)

## Hardware Design

* [Apple2fpga: Reconstructing an Apple II+ on an FPGA](http://www.cs.columbia.edu/~sedwards/apple2fpga/)

## CPUs

### 6502

* [6502.org Tutorials](http://www.6502.org/tutorials/)

* [NesDev 6502 optimizations](https://wiki.nesdev.com/w/index.php/6502_assembly_optimisations) and (synthetic instructions)https://wiki.nesdev.com/w/index.php/Synthetic_instructions)

### Z80

## Programming Tools

## Open-Source BIOSs

* [http://a2go.applearchives.com/roms/](apple][go) - The Apple\]\[Go ROM is a public domain Apple \]\[ replacement ROM that is capable of running most games not requiring Applesoft. This ROM was written in 2006 by Marc Ressl specifically for use with the Apple\]\[Go Emulator

* [https://github.com/MEGA65/open-roms](open-roms) - A project to create unencumbered open-source ROMs for use on selected retro computers

* [http://cbios.sourceforge.net/](CBIOS) - A BSD-licensed MSX BIOS written from scratch by BouKiCHi (no cassette/disk/BASIC yet)

## Misc.

* [Lou's Psuedo-3D Page](http://www.extentofthejam.com/pseudo/) - How to draw 3-D roads

http://www.bjars.com/resources.html

http://www.bjars.com/disassemblies.html

http://atariage.com/forums/topic/199249-video-life-without-flicker-how/

http://alienbill.com/2600/basic/music/tune2600.html

http://alienbill.com/2600/playfieldpal.html

## Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](CONTRIBUTING.md) first.

