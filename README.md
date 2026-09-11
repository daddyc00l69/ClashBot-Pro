# Auto Clash - Decompiled & Recovered Source Project

## Overview
This repository contains the thoroughly reverse-engineered, decompiled, and recovered source code, assets, configuration, dependencies, metadata, and technical analysis for the Windows executable **AutoClash** (`AutoClash.exe`).

The binary was compiled using **Nuitka Onefile** (packing 1,202 embedded payload files with Zstandard compression) and obfuscated with **PyArmor 7/8** before being compiled into native C/C++ x86-64 machine code in `gui.dll`.

This recovery reconstructs the original project hierarchy, packaging structure, Python modules, PySide6 GUI elements, template matching assets, and configuration systems without redesigning or reimplementing the original logic.

---

## Directory Structure

```text
C:\Users\aradh\Desktop\Auto Clash clone Vip\
├── Recovered_Source\
│   ├── Source\                           # Recovered Python application modules
│   │   ├── pyarmor_runtime_015394\       # Bundled PyArmor native runtime extension
│   │   ├── attack\                       # Attack algorithms & deployment coordinates
│   │   │   ├── __init__.py
│   │   │   ├── attacklogic.py            # Battle state machine & combat sequencing
│   │   │   ├── barchgob.py               # Barbarian / Archer / Goblin strategy
│   │   │   ├── dragon.py                 # Dragon assault automation
│   │   │   ├── edragon.py                # Electro Dragon chain-lightning attack logic
│   │   │   ├── fourside_coords.py        # 4-side perimeter coordinate grid
│   │   │   ├── geometry.py               # Coordinate transformations and tile math
│   │   │   ├── sbarb.py                  # Sneaky Barbarian deployment
│   │   │   ├── sminion.py                # Sneaky Minion deployment
│   │   │   ├── threeside_coords.py       # 3-side perimeter coordinate grid
│   │   │   ├── thrower.py                # Siege machine & thrower tactics
│   │   │   ├── valkyrie.py               # Valkyrie deployment
│   │   │   ├── valkyrie_1side.py         # Valkyrie single-side funnel strategy
│   │   │   ├── war_onestar.py            # Clan War safe 1-star strategy
│   │   │   └── war_twothreestar.py       # Clan War 2/3-star optimization strategy
│   │   ├── builder_base\                 # Builder Base automation subsystem
│   │   │   ├── __init__.py
│   │   │   ├── functions.py              # Clock tower boost, cart collection, gem mine
│   │   │   ├── main.py                   # Builder Base loop orchestrator
│   │   │   ├── vision_builder.py         # Builder Base template detection & OCR
│   │   │   └── walls.py                  # Builder Base wall upgrading
│   │   ├── profiles\                     # Profile & config management
│   │   │   ├── __init__.py
│   │   │   ├── config_manager.py         # JSON config loader, parser & schema validator
│   │   │   └── profile_manager.py        # Multi-village switcher & account profiles
│   │   ├── ui\                           # PySide6 (Qt6) Graphical User Interface
│   │   │   ├── __init__.py
│   │   │   ├── gui.py                    # Qt Application bootstrap & theme setup
│   │   │   ├── main_window.py            # Primary desktop dashboard & tab views
│   │   │   ├── mini_window.py            # Floating compact monitoring widget
│   │   │   ├── activation_window.py      # License activation dialog & HWID prompt
│   │   │   ├── account_creation_worker.py# Background Supercell ID account creator
│   │   │   ├── bot_worker.py             # Main QThread executing the bot lifecycle
│   │   │   ├── stats_store.py            # Real-time loot & raid statistics tracker
│   │   │   └── i18n.py                   # Localization manager (11 languages)
│   │   ├── utils\                        # Utility subsystems
│   │   │   ├── __init__.py
│   │   │   ├── multitouch.py             # Multi-point touch gesture generator
│   │   │   ├── profile_backup.py         # Automatic configuration backup & restore
│   │   │   └── runtime_paths.py          # Portable path resolution & temp cleanup
│   │   ├── actions.py                    # In-game click, drag, zoom, and swipe macros
│   │   ├── adb.py                        # ADB communication bridge (port 5556, etc.)
│   │   ├── army_update.py                # Barracks queue & troop training monitor
│   │   ├── auto_place_building.py        # Automatic building placement
│   │   ├── auto_place_walls.py           # Automatic wall placement & segmenting
│   │   ├── bb_obstacle_removal.py        # Builder Base obstacle clearing
│   │   ├── builder_boat.py               # Village navigation via Builder's Boat
│   │   ├── capital_raid.py               # Clan Capital weekly raid automation
│   │   ├── clangames.py                  # Clan Games task picker & auto-completer
│   │   ├── collect_achievements.py       # Gem collector for completed achievements
│   │   ├── control.py                    # Process lifecycle & stop/pause signals
│   │   ├── create_profile.py             # Profile creation wizard logic
│   │   ├── defaults.py                   # Master configuration settings & defaults
│   │   ├── donations.py                  # Clan Castle donation & spell request bot
│   │   ├── error_popup_watcher.py        # Disconnect, maintenance & error handler
│   │   ├── farming.py                    # Multiplayer search, loot evaluation & attack
│   │   ├── findblacksmith.py             # Blacksmith structure detection
│   │   ├── findcc.py                     # Clan Castle detection
│   │   ├── fixed_points.py               # Screen UI anchors & coordinate definitions
│   │   ├── gui.py                        # Application entry bootstrap
│   │   ├── license_manager.py            # License verification & HWID cryptosystem
│   │   ├── main.py                       # Top-level execution entry point
│   │   ├── main_window.py                # Main window layout definitions
│   │   ├── multitouch.py                 # Multi-touch emulation helper
│   │   ├── obstacle_removal.py           # Home Village obstacle removal loop
│   │   ├── process.py                    # Process inspection & emulator watcher
│   │   ├── ranked.py                     # Trophy pushing & league attack runner
│   │   ├── recovery.py                   # Desync recovery & game relauncher
│   │   ├── request_and_leave.py          # 'Req and Leave' clan hopping engine
│   │   ├── rush_th.py                    # Fast Town Hall upgrading algorithm
│   │   ├── startup.py                    # Application pre-flight check & updater
│   │   ├── stats.py                      # Session statistics calculation
│   │   ├── ui2_zoom.py                   # Automatic pinch-to-zoom calibration
│   │   ├── updater_helper.py             # Remote version checker & patcher
│   │   ├── upgrades_research.py          # Laboratory research & builder allocator
│   │   ├── vision.py                     # OpenCV template matching & OCR engine
│   │   ├── walls.py                      # Wall upgrade scanner & resource dumper
│   │   ├── war.py                        # Clan War attack automation
│   │   └── weekly_deal.py                # Trader shop deals & medal redeemer
│   ├── Resources\
│   │   ├── assets\                       # UI icons, SVG arrows, checkboxes, icon.ico
│   │   ├── templates\                    # 992 OpenCV visual template images
│   │   └── locales\                      # 11 language translation files (.json)
│   ├── Config\
│   │   ├── bot.config                    # Window geometry & emulator state
│   │   ├── license.key                   # Client license key
│   │   ├── profiles\                     # Village profile configs (config.json)
│   │   └── treasureloot\                 # Loot thresholds & priorities
│   ├── Dependencies\
│   │   ├── Tools\                        # adb, tesseract OCR, uiautomator2 binaries
│   │   ├── wheels_manifest.json          # Python package inventory
│   │   ├── native_dlls_manifest.json     # 97 .pyd and 50 .dll inventory
│   │   └── requirements.txt              # Pip requirements file
│   ├── Metadata\
│   │   ├── pe_headers.json               # PE header records
│   │   ├── sections.json                 # Section addresses, sizes, and entropy
│   │   ├── exports_imports.json          # DLL exports and imports
│   │   ├── nuitka_version_info.json      # Nuitka compilation details
│   │   └── file_hashes_sha256.json       # SHA-256 integrity hashes
│   ├── Analysis\
│   │   ├── constants_dump\               # Per-module JSON constants pools
│   │   ├── nbc_disassembly\              # Nuitka bytecode and module tables
│   │   ├── module_hierarchy.json         # Introspected classes, methods, and functions
│   │   └── strings_inventory.txt         # Extracted printable strings inventory
│   └── Project\
│       ├── pyproject.toml                # Project packaging configuration
│       ├── requirements.txt              # Virtualenv requirements
│       ├── run.py                        # Project launcher
│       └── setup_env.bat                 # Automated virtual environment installer
├── README.md                             # High-level project documentation (this file)
├── ANALYSIS.md                           # In-depth reverse-engineering technical paper
├── DEPENDENCIES.md                       # Comprehensive dependency & toolchain audit
└── RECOVERY_REPORT.md                    # Detailed recovery verification report
```

---

## Technical Prerequisites

To execute or inspect the recovered project:
- **Operating System:** Windows 10 / Windows 11 (64-bit)
- **Python Version:** Python 3.10.x 64-bit (`Python 3.10.11` recommended)
- **Android Emulator:** BlueStacks 5 (Nougat 32/64 or Pie 64) or LDPlayer 9 with ADB debugging enabled.
- **Resolution:** 860x480 or 1280x720 (DPI 160) recommended for emulator screen matching.

---

## Quick Start & Setup

### 1. Automated Setup (Recommended)
Open a terminal in `Recovered_Source\Project\` and run:
```bat
setup_env.bat
```
This script creates a Python 3.10 virtual environment, upgrades `pip`, and installs all necessary packages.

### 2. Manual Setup
```bash
cd "C:\Users\aradh\Desktop\Auto Clash clone Vip\Recovered_Source\Project"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Launching
```bash
python run.py
```
Or import any module directly from Python:
```python
import sys
sys.path.insert(0, r"C:\Users\aradh\Desktop\Auto Clash clone Vip\Recovered_Source\Source")

import defaults
print("Default attack strategy:", defaults.SELECTED_ATTACK_STRATEGY)
```

---

## Core Features & Subsystems

1. **Multiplayer Farming (`farming.py`, `attack/`)**:
   - Automated matchmaking search with minimum Gold, Elixir, and Dark Elixir filters.
   - Attack deployment strategies: Barch/Goblin, Sneaky Goblin, Dragon, Electro Dragon, Valkyrie, and Thrower.
   - Town Hall star targeting and automatic battle surrender when target stars/loot are obtained.

2. **Clan Automation (`donations.py`, `request_and_leave.py`, `clangames.py`, `war.py`)**:
   - Auto-detection of donation requests in clan chat.
   - Smart spell and troop donation matching.
   - Clan Games automated challenge selection and progression.
   - Clan War attack scheduling and Town Hall cleanup.

3. **Builder Base (`builder_base/`, `bb_obstacle_removal.py`)**:
   - Clock Tower boost activation.
   - Automatic Baby Dragon deployment and star harvesting.
   - Obstacle clearing and Gem Mine collection.

4. **Vision & OCR (`vision.py`, `findcc.py`, `findblacksmith.py`)**:
   - High-performance multi-scale OpenCV template matching across 992 template images.
   - Tesseract OCR for text reading, upgrade timers, and resource values.

5. **Licensing & Protection (`license_manager.py`, `ui/activation_window.py`)**:
   - Client-side hardware identifier (HWID) generation using CPU and motherboard UUIDs.
   - Key verification format: `AC-XXXXX-XXXXX-XXXXX-XXXXX`.
