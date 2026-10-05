# ⚔️ Auto Clash - Recovered Source (Base Version / v1.0)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10.11-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-PySide6%20%2F%20Qt6-41CD52.svg?logo=qt&logoColor=white)](https://www.qt.io/)
[![Vision](https://img.shields.io/badge/Vision-OpenCV%20%26%20Tesseract-5C3EE8.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![Status](https://img.shields.io/badge/Status-100%25%20Recovered-success.svg)](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/RECOVERY_REPORT.md)

**Complete decompiled, carved, and verified source tree recovered from the base binary (`AutoClash.exe`, 97,402,368 bytes).**

</div>

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Module Architecture & Inventory](#-module-architecture--inventory)
- [Subsystems Breakdown](#-subsystems-breakdown)
- [Assets & Templates](#-assets--templates)
- [Decrypted Fixed Points](#-decrypted-fixed-points)
- [How to Run](#-how-to-run)
- [Integrity & Verification](#-integrity--verification)

---

## 🌟 Overview

This directory houses the complete recovered source code, assets, configurations, and toolchain dependencies for the base release of **Auto Clash**.

- **Source Executable:** `AutoClash.exe` (97,402,368 bytes, SHA-256: `6886e8ea3f3f...`)
- **Extracted Payload:** 1,202 files (314.43 MB uncompressed)
- **Core DLL:** `gui.dll` (94,558,208 bytes)
- **Application Modules:** 76 modules protected via PyArmor runtime `015394`
- **Visual Templates:** 992 OpenCV PNG template images
- **Encrypted Fixed Points:** 862 screen coordinate anchors in `fixed_points_data.enc`

---

## 📦 Module Architecture & Inventory (76 Total)

The application code is divided into 5 core packages and root execution modules:

```
Source/
├── pyarmor_runtime_015394/          # Native PyArmor runtime hook
├── attack/                          # 15 Combat & Deployment algorithms
│   ├── attacklogic.py               # Main battle state coordinator
│   ├── barchgob.py                  # Barbarian & Goblin collector raid
│   ├── dragon.py / edragon.py       # Air assault & funneling
│   ├── fourside_coords.py           # 4-side coordinate generator
│   ├── geometry.py                  # Polygon & tile calculations
│   ├── sbarb.py / sminion.py        # Sneaky Barbarian & Sneaky Minion sniping
│   ├── threeside_coords.py          # 3-side coordinate generator
│   ├── thrower.py                   # Siege machine & thrower line deployment
│   ├── valkyrie.py / valkyrie_1side.py # Core funneling algorithms
│   └── war_onestar.py / war_twothreestar.py # Clan War attack engines
├── builder_base/                    # 5 Builder Base automation modules
│   ├── functions.py                 # Village interaction primitives
│   ├── main.py                      # Loop coordinator & battle finder
│   ├── vision_builder.py            # Builder base template recognition
│   └── walls.py                     # Builder base wall upgrade loop
├── profiles/                        # 3 Profile & multi-village modules
│   ├── config_manager.py            # JSON schema validation & persistence
│   └── profile_manager.py           # Village slot switching & credentials
├── ui/                              # 10 PySide6 Qt6 interface modules
│   ├── account_creation_worker.py   # Supercell ID creation thread
│   ├── activation_window.py         # License key input & HWID display
│   ├── bot_worker.py                # Main QThread coordinating bot routines
│   ├── gui.py                       # QApplication bootstrap & dark styling
│   ├── i18n.py                      # Multi-language string resolver
│   ├── main_window.py               # Master control dashboard & settings
│   ├── mini_window.py               # Floating compact overlay
│   └── stats_store.py               # Session loot & trophies metrics
├── utils/                           # 4 Runtime helper modules
│   ├── multitouch.py                # Multi-touch gesture driver
│   ├── profile_backup.py            # Zip archive backup manager
│   └── runtime_paths.py             # Onefile transient path resolver
└── Root Scripts:
    ├── actions.py                   # Touch primitives (tap, swipe, drag)
    ├── adb.py                       # Socket communication with BlueStacks / LDPlayer
    ├── army_update.py               # Troop training queue monitor
    ├── auto_place_building.py       # Building placement engine
    ├── auto_place_walls.py          # Segmented wall placement
    ├── bb_obstacle_removal.py       # Builder base obstacle clearing
    ├── builder_boat.py              # Transition between Home & Builder base
    ├── capital_raid.py              # Clan Capital weekend raid participation
    ├── clangames.py                 # Clan Games task scheduler & auto-claim
    ├── collect_achievements.py      # Achievement gem harvester
    ├── control.py                   # Pause, stop, resume signals
    ├── create_profile.py            # New profile wizard
    ├── defaults.py                  # Configuration keys & default values
    ├── donations.py                 # Clan Castle donation bot
    ├── error_popup_watcher.py       # Disconnect popup dismisser
    ├── farming.py                   # Multiplayer matchmaker & loot evaluation
    ├── findblacksmith.py            # Blacksmith detection
    ├── findcc.py                    # Clan Castle detection
    ├── fixed_points.py              # Coordinate lookup wrapper
    ├── fixed_points_source.py       # Decrypted coordinate dictionary (862 points)
    ├── gui.py / main.py             # Top-level entry points
    ├── license_manager.py           # HWID generator & license checker
    ├── main_window.py               # Window definitions
    ├── obstacle_removal.py          # Home village obstacle clearing
    ├── process.py                   # Emulator process monitor
    ├── ranked.py                    # Trophy pushing battle loop
    ├── recovery.py                  # Game relauncher & desync recovery
    ├── request_and_leave.py         # Fast clan hopping loop
    ├── rush_th.py                   # Town Hall rushing algorithm
    ├── startup.py                   # Pre-flight check & auto-updater
    ├── stats.py                     # Statistics aggregation
    ├── ui2_zoom.py                  # Pinch-to-zoom calibration helper
    ├── updater_helper.py            # Remote version comparison
    ├── upgrades_research.py         # Laboratory & builder management
    ├── vision.py                    # OpenCV template matcher
    ├── walls.py                     # Wall upgrade & resource dumping
    ├── war.py                       # Clan war attack runner
    └── weekly_deal.py               # Trader shop daily reward redeemer
```

---

## 🎨 Assets & Templates
- **Templates (`Resources/templates/`):** 992 high-precision PNG templates for Town Hall 1–16, troops, defenses, tabs, and Clan Games.
- **Locales (`Resources/locales/`):** 11 language translation JSON files (`ar`, `de`, `en`, `es`, `fr`, `hi`, `id`, `pt-br`, `ru`, `tl`, `tr`).
- **Icons & Assets (`Resources/assets/`):** UI icons, SVG elements, and `fixed_points_data.enc`.

---

## 🔑 Decrypted Fixed Points
All 862 coordinate anchors from `fixed_points_data.enc` have been decrypted via AES-256-GCM and stored in:
[`Source/fixed_points_source.py`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/releases/v1.0-base/Source/fixed_points_source.py)

---

## 🚀 How to Run

1. **Via Batch Launcher:**
   Double-click [`run_v1_base.bat`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/run_v1_base.bat) in the workspace root.

2. **Via Command Line:**
   ```cmd
   cd releases\v1.0-base\Source
   python ..\Project\run.py
   ```

3. **Run Integrity Tests:**
   ```cmd
   cd releases\v1.0-base\Project
   python test_suite.py
   ```
