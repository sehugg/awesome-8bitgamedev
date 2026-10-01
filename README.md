# Awesome 8-bit Game Dev

A curated list of awesome resources for 8-bit retro game development.

## Table of Contents

- [Home Consoles](#home-consoles)
  - [Fairchild Channel F](#fairchild-channel-f)
  - [Bally Astrocade](#bally-astrocade)
  - [Atari 2600](#atari-2600)
  - [APF MP-1000](#apf-mp-1000)
  - [Magnavox Odyssey²](#Magnavox-Odyssey²)
  - [Intellivision](#intellivision)
  - [ColecoVision](#colecovision)
  - [Vectrex](#vectrex)
  - [NES](#nes)
  - [Atari 5200](#atari-5200)
  - [Atari 7800](#atari-7800)
  - [Sega Master System](#sega-master-system)
  - [Game Boy](#game-boy)
  - [PC Engine](#pc-engine)
  - [Atari Lynx](#atari-lynx)
- [Home Computers](#home-computers)
  - [Apple I](#apple-i)
  - [Commodore PET](#commodore-pet)
  - [TRS-80](#trs-80)
  - [Apple II/II+/IIe](#apple-ii)
  - [Atari 400/600/800/XL/XE](#atari-8-bit)
  - [TI 99/4](#ti-99-4)
  - [Commodore VIC-20](#commodore-vic-20)
  - [Acorn](#acorn)
  - [Oric](#oric)
  - [TRS-80 CoCo and Dragon](#trs-80-coco-and-dragon)
  - [Sinclair](#sinclair)
  - [Commodore 64](#commodore-64)
  - [MSX](#msx)
  - [Amstrad CPC](#cpc)
- [Arcade Games](#arcade-games)
- [Hardware](#hardware)
  - [6502](#6502)
  - [Z80](#z80)
  - [TMS9918A](#tms9918a)
  - [FPGA/HDL](#fpga-hdl)
  - [Microcontrollers](#microcontrollers)
- [Development Tools](#development-tools)
  - [Assemblers](#assemblers)
  - [Compilers](#compilers)
  - [Emulators](#emulators)
  - [IDEs](#ides)
  - [Graphics](#graphics)
  - [Music and Sound](#music-and-sound)
  - [Libraries](#libraries)
- [BASIC Programming](#basic)
- [Books](#books)
- [Community](#community)
- [Contributing](#contributing)

## Home Consoles

### Fairchild Channel F

* [VES Wiki](https://channelf.se/veswiki/index.php?title=Main_Page) and [tutorial](https://channelf.se/veswiki/index.php?title=Tutorial:Beginner%27s_Guide_to_the_Channel_F)

* [Sean Riddle's Channel F Info](https://seanriddle.com/chanfinfo.html) including a homebrew Tetris clone

* [Fairchild F8 Info](https://www.nyx.net/~lturner/public_html/Fairchild_F8.html) and [instruction set](https://www.nyx.net/~lturner/public_html/F8_ins.html)

### Bally Astrocade

* [Bally Alley](https://ballyalley.com/) - An archive of all things Bally Astrocade.

* [The Better Bally Book](http://metopal.com/projects/ballybook/doku.php) - A wiki dedicated to organizing, annotating, and improving Software and Hardware for the Bally Arcade, a technical manual for the Bally Home Computer/Arcade/Astrocade originally published in 1978 by Dave Nutting Associates. 

* [hxlnt's Astrocade Dev](https://github.com/hxlnt/astrocade) - Z80 demos and graphics tools for the Astrocade. Also see this [thread](https://atariage.com/forums/topic/251416-programming-the-bally-arcadeastrocade/).

### Atari 2600

* [Stella Programmer's Guide](https://alienbill.com/2600/101/docs/stella.html) - The official guide to programming the Atari 2600, from Atari employee Steve Wright. 

* [Atari 2600 Advanced Programming Guide](https://www.qotile.net/minidig/docs/2600_advanced_prog_guide.txt) - Paul Slocum compiled this list of Atari 2600 programming techniques, including an HMOVE timing chart.  Also see this [list of tricks](https://www.qotile.net/minidig/tricks.html).

* [TIA Hardware Notes](https://www.atarihq.com/danb/files/TIA_HW_Notes.txt) - A detailed analysis of the TIA chip by Andrew Towers.

* [Kirk Israel's 2600 Programming Page](https://alienbill.com/2600/) - A bunch of links by a 2600 homebrew developer. Also see his [2600 Cookbook](https://alienbill.com/2600/cookbook/),
[webTune2600](https://alienbill.com/2600/basic/music/tune2600.html),
and
[playfieldpal](https://alienbill.com/2600/playfieldpal.html) tools

* [Random Terrain 2600 Page](https://www.randomterrain.com/atari-2600-memories.html) - Includes [Atari 2600 Programming for Newbies](https://www.randomterrain.com/atari-2600-memories-tutorial-andrew-davie-01.html), batariBasic info, programming tools, and much more.

* [BJARS Atari Archives](https://web.archive.org/web/20230926210554/http://bjars.com/) - Steve Engelhardt's site full of homebrew, hacks, online tools, references, and disassembled code.

* [Stellerator](https://6502ts.github.io/typedoc/stellerator-embedded/) - An online Atari 2600 emulator.

### AFP MP-1000

* [AFP MP-1000 Programming](https://orphanedgames.com/APF/index.html) - AFP/6800 programming tools for Windows, and documentation.

### Magnavox Odyssey²

* [Dan B's Odyssey 2 Tech Page](https://atarihq.com/danb/o2.shtml) - Hardware information, including the [Odyssey 2 Technical Specs](https://atarihq.com/danb/files/o2doc.pdf) (PDF).

* [AtariAge Odyssey 2 Programming Thread](https://forums.atariage.com/topic/130697-odyssey-2-programming/) - Starting point for programming the Intel 8048 and 8244 VDC.

### Intellivision

* [jsintv](http://spatula-city.org/~im14u2c/intv/) - Portable Intellivision emulator and programming tools

* [IntyBASIC](https://nanochess.org/intybasic.html) - a BASIC compiler for Intellivision

### ColecoVision

* [ColecoVision Tech Info](https://www.atarihq.com/danb/files/CV-Tech.txt) and [Sound Info](https://www.atarihq.com/danb/files/CV-Sound.txt).

* Philipp Klaus Krause's [tutorial](http://www.colecovision.eu/ColecoVision/development/tutorial1.shtml) on using [libCV](http://www.colecovision.eu/ColecoVision/development/libcv.shtml) to develop games in C using SDCC. Also includes graphics conversion and compression tools.

* [ColecoVision.dk](https://www.colecovision.dk/tools.htm) - Tools and homebrew source code.

## Vectrex

* [Setting up a modern toolchain for Vectrex development with CMOC](https://optixx.org/2019/11/02/a-modern-toolchain-for-vectrex-development/)

### Sega SG-1000

* [Sega Game 1000 Specifications](https://www.smspower.org/uploads/Development/sg1000.txt) - by Omar Cornut / Zoop

### NES

* [NesDev Wiki](https://www.nesdev.org/wiki/Nesdev_Wiki) - Comprehensive site with NES programming tutorials, reference guides, and homebrew.

* [Shiru's Stuff](https://shiru.untergrund.net/software.shtml) - Shiru has lots of NES programming tools, and the article [programming NES games in C](https://shiru.untergrund.net/articles/programming_nes_games_in_c.htm).

* [Dustmop's NES Graphics](https://www.dustmop.io/blog/2015/04/28/nes-graphics-part-1/) - Describes NES graphics in detail.

* [nesdoug](https://nesdoug.com/) - Step-by-step tutorial on making a NES game in C.

* [Lizard NES](https://lizardnes.com/) - Homebrew game with a great development blog.

* [Mega Cat Studios](https://megacatstudios.com/blogs/retro-development/organizing-nes-graphics-banks) - Some good blog posts about efficiently managing NES graphics assets.

* [Nerdy Nights](https://fuzzytek.net/articles/nerdynights/) NES programming tutorials

* [Famicom Party](https://famicom.party/book/) - Making NES Games in Assembly (book, in progress)

* [FamiStudio](https://famistudio.org/) - NES Music Editor
  
* [NESFab](https://pubby.games/nesfab.html) - A NES-specific programming language with advanced 6502 optimizations and automatic bank placement.

### Atari 5200

* [Dan B's Atari 5200 Page](https://www.atarihq.com/danb/a5200.shtml) - System specs, technical documentation, and links.

* [Atari 5200 Programmers](https://atariage.com/programmer_list.php?SystemID=5200) - AtariAge's list of 5200 programmers and games.

* The 5200 shares ANTIC, GTIA, and POKEY with the [Atari 8-bit](#atari-8-bit) computers, so those references apply too.

### Atari 7800

* [Atari 7800 (Dan Boris)](https://atarihq.com/danb/a7800.shtml) - System Specs, Cartridge Information, Links, The 'Encryption' Issue, Technical Files, and more.

* [Atari 7800 Software Guide](https://7800.8bitdev.org/index.php/7800_Software_Guide) - 7800 hardware description, registers, DMA timing, and more.

* [Atari 7800 Programming Wiki](https://sites.google.com/site/atari7800wiki/) - This site is intended to be a reference for the Atari 7800 Programming mailing list, with information culled from the mailing list archives and other sources (i.e. Atari Age forums)

* [CC7800](https://github.com/steux/cc7800) - A C-inspired compiler for the Atari 7800.
 
### Sega Master System

* [SMS Power](https://www.smspower.org/Development/Index) - This area is dedicated to studying, programming, hacking of Sega 8-bit hardware and software.
[Technical info](https://www.smspower.org/uploads/Development/richard.txt), 
[VDP info](https://www.smspower.org/uploads/Development/msvdp-20021112.txt),
[SN76489 sound chip info](https://www.smspower.org/uploads/Development/SN76489-20030421.txt)

* [devkitSMS](https://github.com/sverx/devkitSMS) - C libraries and tools for SDCC targeting the Master System, Game Gear, SG-1000, SC-3000, and ColecoVision.

### Game Boy

* [Pan Docs](https://gbdev.io/pandocs/) - The most comprehensive Game Boy technical reference.

* [GB Dev](https://gbdev.io/) - Community hub with [awesome-gbdev](https://github.com/gbdev/awesome-gbdev), [RGBDS](https://rgbds.gbdev.io/), a [GB ASM Tutorial](https://gbdev.io/gb-asm-tutorial/), and the [Homebrew Hub](https://hh.gbdev.io) game archive.

* [GBDK-2020](https://github.com/gbdk-2020/gbdk-2020) - C compiler, libraries, and tools for the Game Boy, Game Boy Color, Master System, Game Gear, and NES.

### PC Engine

* [pce-dev-kit](https://github.com/langel/pce-dev-kit/) - PC Engine / TurboGrafx-16 development archive of documentation, tools, and examples.

* [HuC-Next](https://github.com/alx5962/hucnext) - HuC C compiler and PCEAS assembler for the HuC6280, packaged with a visual game maker.

### Atari Lynx

* [Atari Lynx Programming Tutorial](https://github.com/AtariLynx/programming-tutorial) - Tutorial series using the cc65 toolchain.

* [Atari Lynx Dev Wiki](https://atarilynxdev.net/doku.php/lynx:compilers) - Compilers and other development information.

* [AtariAge Lynx Programming Forum](https://forums.atariage.com/forum/53-atari-lynx-programming/)

## Home Computers

### Apple I

* [Understanding the Apple I](https://www.applefritter.com/replica/chapter7)

* Signetics [2513](https://www.applefritter.com/files/signetics2513.pdf), [2504](http://retro.hansotten.nl/uploads/6502docs/signetics2504.pdf), and [2519](http://retro.hansotten.nl/uploads/6502docs/signetics2519.pdf) datasheets

### Commodore PET

* [Commodore PET Programming Model](https://6502.org/users/andre/petindex/progmod.html) - The PET's memory map.

### TRS-80

### Apple II

* [The Big PEEKs, POKEs and CALLs list](https://apple2.org.za/gswv/USA2WUG/FOUNDING.MEMBERS/HOME.PAGES/EDHEL/texts/pokes.html) - Compiled by Edhel Iaur, Esq.

* [HIRES Graphics on Apple II](https://www.xtof.info/blog/?p=768) - Detailed explanation of the Apple II's convoluted graphics scheme, including the [Rgb2Hires](https://github.com/Pixinn/Rgb2Hires) conversion utility.

### Atari 8-bit

* [ANTIC, GTIA and timing info](https://www.atarimax.com/jindroush.atari.org/atanttim.html)

* [Reverse engineering Atari 8-bit video](https://www.virtualdub.org/blog/pivot/entry.php?id=243)

* [ANTIC Timings](http://www.beipmu.com/Antic_Timings.txt)

* [ANTIC Registers](https://user.xmission.com/~trevin/atari/antic_regs.html) and [Instructions](https://user.xmission.com/~trevin/atari/antic_insns.html); [GTIA Registers](https://user.xmission.com/~trevin/atari/gtia_regs.html)

* [TRANSPORTING ATARI COMPUTER PROGRAMS TO THE ATARI 5200](https://www.atarimuseum.com/videogames/consoles/5200/conv_to_5200.html) - A.N.A.L.O.G. #15, January 1984

* [Atari Cartridge Images](https://github.com/dmlloyd/atari800/blob/master/DOC/cart.txt)

* [Atari 5200 Memory Map](http://atariage.com/forums/topic/169971-5200-memory-map/)

* [Player/Missile Podcast Tutorials](https://playermissile.com/index.html#tutorials)

* [Altirra Hardware Reference Manual](https://www.virtualdub.org/downloads/Altirra%20Hardware%20Reference%20Manual.pdf)

### TI 99/4

### Commodore VIC-20

### Acorn

* [The BBC and Master Computer Public Domain Library](https://8bs.com/) and [8-Bit Acorn Webring](https://8bs.com/webring.htm) (Webrings still exist?!?)

* [Acorn Atom Technical Manual](https://chrisacorns.computinghistory.org.uk/docs/Acorn/Manuals/Acorn_AtomTechnicalManual.pdf) (PDF)

### Oric

* [Oric Software Development Kit](https://github.com/Oric-Software-Development-Kit/osdk) - Cross-development tools for the Oric, including a C compiler, assembler, linker, and disk and tape utilities.

* [Defence Force Oric Library](https://library.defence-force.org) - Manuals, schematics, and other documentation for the Oric line.

### TRS-80 CoCo and Dragon

* [Platform Guide: TRS-80 Color Computer/Dragon](https://bumbershootsoft.wordpress.com/platform-guide-trs-80-color-computer-dragon/) - Overview of the hardware, tools, and documentation.

* [XRoar](https://www.6809.org.uk/xroar/) - Emulator for the Dragon 32/64, Tandy Color Computers 1-3, and the MC-10.

* [ChibiAkumas 6809 Tutorials](https://www.chibiakumas.com/6809/) - 6809 assembly lessons for the Dragon/CoCo, Fujitsu FM-7, and Vectrex.

### Sinclair

* [World of Spectrum](https://www.worldofspectrum.org/) - The official world archive for the Sinclair ZX Spectrum and the largest on-line gaming center on the Internet (*Yup, I think the site's great - Cliff Lawson*)

* [16K/48K ZX Spectrum Reference](https://www.worldofspectrum.org/faq/reference/48kreference.htm#ZXSpectrum) and [128K](https://www.worldofspectrum.org/faq/reference/128kreference.htm)

* [How to Write ZX Spectrum Games](https://chuntey.wordpress.com/2012/12/18/how-to-write-zx-spectrum-games-chapter-1/) - Converting a simple BASIC program to Z80, by Jonathan Cauldwell

### Commodore 64

* [C64 Wiki](https://www.c64-wiki.com/wiki/C64)

* [Codebase64](https://codebase64.net/) - Wiki of C64 programming articles, source code, and hardware documentation.

* [C64 Programmer's Reference Guide](https://www.zimmers.net/cbmpics/cbm/c64/c64prg.txt)

* [The MOS 6567/6569 video controller (VIC-II)](https://www.zimmers.net/cbmpics/cbm/c64/vic-ii.txt)

* [C64 Memory Map](https://sta.c64.org/cbm64mem.html)

* [accurately reproducing the Video Output of a Commodore C64](https://hitmen.c02.at/temp/palstuff/)

* [The CIA 6526](https://www.c64-wiki.com/wiki/CIA)

* [Reading the C64 Keyboard](https://codebase64.net/doku.php?id=base:reading_the_keyboard) and [How the C64 Keyboard Works](https://www.c64os.com/post/?p=45)

* [Ultimate C64 Reference](https://www.pagetable.com/c64ref/c64mem/)

* [C64 Memory Maps](http://unusedino.de/ec64/technical/project64/memory_maps.html)

* [TinyBubbles](https://github.com/SPixs/TinyBubbles) - Open-source 4 KB C64 game in 6502 assembly, with a write-up of its size tricks (autostart via the stack, raster IRQ, SID noise as RNG).

### MSX

* [MSX Wiki](https://www.msx.org/wiki/)

* [MSX Assembly Page](https://map.grauw.nl/)

* [Konamiman's MSX page](https://github.com/Konamiman/MSX2-Technical-Handbook)

* [The MSX Red Book](https://github.com/gseidler/The-MSX-Red-Book/blob/master/the_msx_red_book.md) - The aim of this book is to provide a description of the standard MSX hardware and software at a level of detail sufficient to satisfy that most demanding of users, the machine code programmer.

* [awesome-msx](https://github.com/fr3nd/awesome-msx) - an awesome list about MSX!

### CPC

* [cpctelera](https://github.com/lronaldo/cpctelera) - Amstrad CPC game engine for C and Assembler developers, integrated into 8bitworkshop

## Arcade Games

* [Computer Archeology](https://www.computerarcheology.com/Arcade/) - Investigating Asteroids, Crazy Climber, Defender, Frogger (Sound), Galaga, Moon Patrol, Omega Race, Space Invaders, Time Pilot (Sound) and the [Asteroids Digital Vector Generator](https://www.computerarcheology.com/Arcade/Asteroids/DVG.html)

* [Programming the Atari XY Vector Generator](https://arcarc.xmission.com/Tech/neilw_xy.txt)

* Jed Margolin's [The Secret Life of Vector Generators](https://www.jmargolin.com/vgens/vgens.htm) and [The Secret Life of XY Monitors](https://www.jmargolin.com/xy/xymon.htm)

* [Sean Riddle's Williams Game Hardware Info](https://seanriddle.com/willhard.html)

## Hardware

### 6502

* [6502.org Tutorials](https://6502.org/tutorials/)

* [6502 instruction set](https://www.masswerk.at/6502/6502_instruction_set.html)

* [NesDev 6502 optimizations](https://www.nesdev.org/wiki/6502_assembly_optimisations) and [synthetic instructions](https://www.nesdev.org/wiki/Synthetic_instructions)

* [6502/6510 Maths](https://codebase64.net/doku.php?id=base:6502_6510_maths)

### Z80

* Z80 Heaven - [Tutorials](https://z80-heaven.wikidot.com/system:tutorials) and [instruction set](https://z80-heaven.wikidot.com/instructions-set)

* [Z80 instruction set](https://clrhome.org/table/) - Searchable table

### TMS9918A

* [Texas Instruments TMS9918A VDP](http://bifi.msxnet.org/msxnet//tech/tms9918a.txt) info by Sean Young. Also see [here](https://www.unige.ch/medecine/nouspikel/ti99/tms9918a.htm).

* [VDP Programming Tutorial](https://map.grauw.nl/articles/vdp_tut.php) - Examples of programming the TMS9918A/v9938/v9958 from Z80 assembly language on the MSX.

* [Convert9918](https://github.com/tursilion/convert9918) - (Windows) This program can convert most modern graphics into a form compatible with the TMS9918A bitmap mode.

* [High-Resolution Sprite-Oriented Color Graphics](https://www.classiccmp.org/cini/pdf/byte/Hi-Res%20Graphics%20TMS9918%20BYTE%200882.pdf.pdf) - Ciarcia's Circuit Cellar column in August 1982 BYTE Magazine about the TMS9918.

### AY-3-8910

* [AY-3-8910 Datasheet](https://map.grauw.nl/resources/sound/generalinstrument_ay-3-8910.pdf) - Datasheet for the programmable sound generator.

### FPGA/HDL

* [ATARI PONG E CIRCUIT ANALYSIS & LAWN TENNIS: BUILDING A DIGITAL VIDEO GAME WITH 74 SERIES TTL IC’s.](https://www.pong-story.com/LAWN_TENNIS.pdf) (PDF) - A detailed analysis of the PONG circuits by Dr. H. Holden.

* [Apple2fpga: Reconstructing an Apple II+ on an FPGA](https://www.cs.columbia.edu/~sedwards/apple2fpga/)

* [fpga-examples](https://github.com/sehugg/fpga-examples) - These are some of the Verilog examples from the book "Designing Video Game Hardware in Verilog" ported to CRT monitor timing and tested against the IceStorm tools.

* [Silice](https://github.com/sylefeb/Silice) - A language for designing FPGA hardware, with retro game and video examples.

* [Verilator](https://www.veripool.org/wiki/verilator) - Fast open-source Verilog simulator, used by 8bitworkshop for hardware simulation.

### Microcontrollers

* [Uzebox](https://uzebox.org/) - An open-source micro game platform based on the ATmega644 chip.

## Development Tools

### Compilers

* [CC65](https://cc65.github.io/) - a C compiler, linker, and assembler for 6502 machines. Targets Commodore, Apple II, Atari 8-bit, NES, and more.

* [SDCC](https://sourceforge.net/p/sdcc/wiki/z80/) - Small Device C Compiler and toolchain. Targets Z80 and Gameboy Z80, among others.

* [z88dk](https://www.z88dk.org/forum/) - A Z80 C and assembly toolchain.
There are two C compilers supported (sccz80 and sdcc), two independent C libraries included (the classic and new), an assembler/linker/librarian (z80asm), and a data compression tool (zx7).
Targets over 80 different machine families.

* [CMOC](https://perso.b2b2c.ca/~sarrazip/dev/cmoc.html) - A 6809 cross-compiler for a subset of the C language. Depends on the [LWTOOLS](https://www.lwtools.ca/) toolchain.

* [batariBASIC](https://github.com/batari-Basic/batari-Basic) - BASIC programming for Atari 2600 systems.

* [LLVM-MOS SDK](https://github.com/llvm-mos/llvm-mos-sdk) - A clang-based compiler/SDK for 6502 systems.

* [GBDK-2020](https://github.com/gbdk-2020/gbdk-2020) - C compiler, libraries, and tools for sm83, Z80, and 6502 consoles including the Game Boy, Game Gear, and NES.

* [devkitSMS](https://github.com/sverx/devkitSMS) - SDCC-based libraries and tools for Sega 8-bit systems and ColecoVision.

* [Mad Pascal](https://github.com/tebe6502/Mad-Pascal) - A 32-bit Turbo Pascal-style compiler for the Atari 8-bit, C64, and other 6502 systems.

* [ZX Basic](https://github.com/boriel-basic/zxbasic) - A BASIC compiler for the ZX Spectrum that generates Z80 code.

* [Oscar64](https://github.com/drmortalwombat/oscar64/) - A C/C++ compiler for the C64 and other 6502 systems.

* [FastBasic](https://github.com/dmsc/fastbasic) - A fast BASIC interpreter and cross-compiler for the Atari 8-bit.

* [Wiz](https://github.com/wiz-lang/wiz) - A high-level assembly language for the 6502, Z80, SM83, 65816, and other CPUs.

### Assemblers

* [DASM](https://dasm-assembler.github.io/) - a versatile macro assembler with support for several 8-bit microprocessors including MOS 6502 & 6507, Motorola 6803, 68705 & 68HC11, Hitachi HD6303 (extended Motorola 6801), and Fairchild F8. Used most often for Atari 2600 development.

* [NESASM3](https://github.com/camsaul/nesasm) - The O.G. NESasm assembler for NES 6502 assembly.

* [ASM6](https://github.com/freem/asm6f) - 6502 assembler primarily targeted at NES/Famicom development.

* [zmac](https://github.com/sehugg/zmac) - Macro cross-assembler for the Zilog Z80 microprocessor, sometimes used for Astrocade development.

* [Kick Assembler](https://theweb.dk/KickAssembler/) - A Java-based 6502/6510 assembler for the C64 with macros, scripting, and graphics conversion helpers.

* [MADS](https://github.com/tebe6502/Mad-Assembler) - A multi-pass 6502/65816 cross-assembler used mostly for Atari 8-bit development.

* [ACME](https://github.com/sehugg/acme) - A 6502/65C02/65816 cross-assembler popular for C64 development.

* [xa](https://www.floodgap.com/retrotech/xa/) - A 6502/65C02/65816 cross-assembler.

* [Merlin32](https://github.com/apple2accumulator/merlin32) - A 65xx cross-assembler compatible with Merlin syntax for the Apple II and IIgs.

* [vasm](https://github.com/mbitsnbites/vasm-mirror) - A portable multi-CPU assembler with 6502, Z80, and 6809 support.

* [naken_asm](https://github.com/mikeakohn/naken_asm) - An assembler and disassembler for many CPUs and microcontrollers.

### Emulators

* [MAMEDev.org](https://www.mamedev.org/) - Home of the MAME/ MESS mega-emulator.

* [Javatari](https://javatari.org/) - Atari 2600 emulator in JavaScript.

* [JSNES](https://jsnes.org/) - NES emulator in JavaScript.

* [Stella](https://stella-emu.github.io/) - A multi-platform Atari 2600 VCS emulator released under the GNU General Public License (GPL).

* [Mesen](https://www.mesen.ca/) - A high-accuracy NES and Famicom emulator and NSF player for Windows and Linux.

* [VICE](https://vice-emu.sourceforge.net/) - The Versatile Commodore Emulator.

* https://github.com/floooh/chips - Portable C emulation library for C64, CPC and other microcomputers.

* [jsvecx](https://www.twitchasylum.com/jsvecx/) - Vectrex emulator in JavaScript.

* [Altirra](https://www.virtualdub.org/altirra.html) - Atari 8-bit family emulator, includes compatible open-source ROM.

* [JSSpeccy 2](https://github.com/gasman/jsspeccy2) - ZX Spectrum emulator in JavaScript.

* [jspce](https://github.com/yhzmr442/jspce) - PC Engine emulator in JavaScript.

* [XRoar](https://www.6809.org.uk/xroar/) - Emulator for the Dragon, Tandy CoCo, and MC-10.

### IDEs

* [8bitworkshop](https://8bitworkshop.com/) - An online batteries-included IDE targeting home consoles, home computers, arcade games, and Verilog hardware design.

* [8bitworkshop for VS Code](https://marketplace.visualstudio.com/items?itemName=8bitworkshop.8bitworkshop) - The 8bitworkshop IDE as a VS Code extension, with bundled toolchains, emulators, and a debugger.

* [WUDSN](https://www.wudsn.com/index.php/ide) - a free integrated Apple II, Atari 2600, Atari 7800, Atari 8-bit, C64 and NES development plugin for Eclipse

* [NESICIDE](https://github.com/christopherpow/nesicide) - multiplatform IDE for NES, includes FamiTracker support.

* [CBM prg Studio](https://www.c64-wiki.com/wiki/CBM_prg_Studio) - Free C64 IDE for Windows written with C# and VB.NET.

* [Turbo Rascal SE](https://lemonspawn.com/turbo-rascal-syntax-error-expected-but-begin/) - A Pascal -> DASM compiler for 6502/68000 computers -- the C64, C128, VIC-20, PLUS4, NES, PET and Amiga 500.

* [BASIC8](https://paladin-t.github.io/b8/) - A fantasy console supporting a BASIC-like language.

### Graphics

* [Dithertron](https://8bitworkshop.com/dithertron/) - From 8bitworkshop. Downsamples/reduces/converts images into many different retro formats, with lots of tweaking options.

* [mcDRAW](https://mcdraw.xyz/) - Cool online bitmap editor for C-64.

* [retropixels](https://www.npmjs.com/package/retropixels) - A command-line tool and library that converts to C-64 format.

* [Tiled](https://www.mapeditor.org/) - A free and flexible tile map and level editor.

### Music and Sound

* [Furnace](https://github.com/tildearrow/furnace) - A multi-system chiptune tracker supporting over 50 sound chips and DefleMask modules.

* [GoatTracker 2](https://sourceforge.net/projects/goattracker2/) - A C64 SID music tracker.

* [vgm2vgr3](https://github.com/8bitws/vgm2vgr3) - Compresses VGM chiptune files into a compact register format with 6502 and Z80 decoders, for the NES, Game Boy, ColecoVision, C64, Atari POKEY, and MSX.

### Libraries

* [CROSS-LIB](https://github.com/Fabrizio-Caruso/CROSS-LIB) - Cross platform game library for several 8/16/32-bit computers.

## Open-Source BIOSs

* [apple2go](https://a2go.applearchives.com/roms/) - The Apple\]\[Go ROM is a public domain Apple \]\[ replacement ROM that is capable of running most games not requiring Applesoft. This ROM was written in 2006 by Marc Ressl specifically for use with the Apple\]\[Go Emulator

* [open-roms](https://github.com/MEGA65/open-roms) - A project to create unencumbered open-source ROMs for use on selected retro computers

* [CBIOS](https://cbios.sourceforge.net/) - A BSD-licensed MSX BIOS written from scratch by BouKiCHi (no cassette/disk/BASIC yet)


* [Altirra](https://www.virtualdub.org/altirra.html) - Contains Atari 8-bit compatible ROM and BASIC interpreter.

## BASIC

* [Altair 8800 Emulator](https://www.ldx.ca/notes/altair-8800-notes.html) and [BASIC disassembly](http://altairbasic.org/)

* [ECMA-55 Minimal BASIC Compiler to x86](https://buraphakit.sourceforge.io/BASIC.shtml)

* [David Ahl's BASIC Computer Games](https://www.atariarchives.org/basicgames/), [more games](http://www.dunnington.info/public/basicgames/)

* [People's Computer Company Archive](https://www.computerhistory.org/collections/catalog/102661095)

* [Dartmouth Time Sharing System Emulator](http://www.dtss.org/dtss/)

* BASIC Manuals - [4th Edition](https://www.bitsavers.org/pdf/dartmouth/dtss/196801_BASIC_4th_Edition.pdf), [OS/8](https://www.grc.com/pdp-8/docs/OS8_BASIC_Reference.pdf), [EduSystem](https://www.bitsavers.org/pdf/dec/pdp8/tss8/EduSystem_Handbook_197301.pdf), [ECMA-55 (Minimal BASIC)](https://buraphakit.sourceforge.io/ECMA-55.TXT.LPR), [BASIC-80](https://altairclone.com/downloads/manuals/Microsoft%20BASIC-80.pdf), [Altair 8800 BASIC 4.1](https://vtda.org/docs/computing/MITS/MITS_Altair8800Basic4.1Reference_April1977.pdf), [HP2000](https://bitsavers.org/pdf/hp/2000TSB/22687-90001_AccessBasic9-75.pdf), [BASIC-PLUS](https://ia801901.us.archive.org/17/items/bitsavers_decpdp11rsSICPLUSLangManOct72_10455777/DEC-11-ORBPA-A-D_BASIC-PLUS_LangMan_Oct72.pdf)


## Books

* [8bitworkshop Books](https://www.amazon.com/s?k=8bitworkshop) - Books that go along with the [8bitworkshop IDE](https://8bitworkshop.com/): "Making Games for the Atari 2600", "Making 8-bit Arcade Games in C", "Making Games for the NES", and "Designing Video Game Hardware in Verilog"

* [Retro Game Dev: C64 Edition](https://www.amazon.com/Retro-Game-Dev-Derek-Morris/dp/0692980652/ref=sr_1_1?keywords=c64+game+dev&qid=1571357742&sr=8-1) - Using modern tools, this introductory book guides you through all the elements required to make two mini games: a space shooter and a platformer, and run them on an emulator or real C64 hardware. Uses CBM prg Studio (Windows IDE)

## Community

* [AtariAge Forums](https://atariage.com/forums/) - Lots of active [programming forums](https://atariage.com/forums/forum/42-game-programming/) for 2600, 5200, 7800, Lynx, Jaguar, ColecoVision, Intellivision, TI-99/4A, homebrew, hacks and more.

* [NesDev Forums](https://forums.nesdev.org/) - Discussion of NES/Famicom programming, emulation, graphics, music, and more.

* [SMS Power Forums](https://www.smspower.org/forums/) - Discussion of all things SEGA!

* [Lemon64](https://www.lemon64.com/forum/index.php) and [EverythingC64](https://everythingc64.boards.net/) - Forums for the C-64 scene.

## Misc.

* [The Digital Antiquarian](https://www.filfre.net/) - Jimmy Maher's blog on the history of computer games and the platforms they ran on

* [Lou's Psuedo-3D Page](https://www.extentofthejam.com/pseudo/) - How to draw 3-D roads

* [8bit-tools](https://github.com/sehugg/8bit-tools/) - Command-line tools that go along with 8bitworkshop books

## Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](CONTRIBUTING.md) first.

