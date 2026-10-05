# ⚔️ Auto Clash - Recovered Source (Update v2.1)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10.11-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-PySide6%20%2F%20Qt6-41CD52.svg?logo=qt&logoColor=white)](https://www.qt.io/)
[![Vision](https://img.shields.io/badge/Vision-OpenCV%20%26%20Tesseract-5C3EE8.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![Version](https://img.shields.io/badge/Release-Update%20v2.1-orange.svg)](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/UPDATE_RECOVERY_REPORT.md)
[![Status](https://img.shields.io/badge/Status-100%25%20Verified%20(80%2F80%20Modules)-success.svg)](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/UPDATE_RECOVERY_REPORT.md)

**Decompiled, carved, and verified source code for the new AutoClash update recovered from `New_Updated_exe\AutoClash.exe` (97,794,560 bytes).**

</div>

---

## 📑 Table of Contents
- [Overview](#-overview)
- [What's New in this Update](#-whats-new-in-this-update)
- [New Application Modules](#-new-application-modules)
  - [1. equipment_upgrade.py](#1-equipment_upgradepy-hero-equipment-automation)
  - [2. rush_bh.py](#2-rush_bhpy-builder-hall-rush-engine)
  - [3. startup_checks.py](#3-startup_checkspy-special-events--dialogue-resolver)
  - [4. ranked_unlock.py](#4-ranked_unlockpy-ranked-battle-unlocker)
- [Complete Module Architecture (80 Modules)](#-complete-module-architecture-80-modules)
- [New Visual Templates (35 Added)](#-new-visual-templates-35-added)
- [Decrypted Fixed Points (906 Total)](#-decrypted-fixed-points-906-total)
- [Directory Layout](#-directory-layout)
- [Quick Start & Execution](#-quick-start--execution)
- [Verification & Integrity](#-verification--integrity)

---

## 🌟 Overview

This directory contains the complete source tree, game assets, configuration templates, and reverse-engineering artifacts recovered from the updated AutoClash binary (`New_Updated_exe\AutoClash.exe`).

- **Target Executable:** `AutoClash.exe` (97,794,560 bytes, x86-64 PE32+)
- **Carved Payload:** 1,237 uncompressed files (314.86 MB)
- **Core Native Module:** `gui.dll` (94,692,864 bytes)
- **Nuitka Constants Blob:** ID #3 at offset `0x04C13F50` (14,910,416 bytes, 880 chunks)
- **Application Modules:** 80 Python modules protected with PyArmor runtime `015394`
- **OpenCV Templates:** 1,026 template images across all game categories
- **Coordinate Anchors:** 906 decrypted screen points in `fixed_points_source.py`

---

## ⚡ What's New in this Update

| Feature | Base Release (v1.0) | New Update (v2.1) | Net Change |
|---|---|---|---|
| **Binary Size** | 97,402,368 bytes | **97,794,560 bytes** | +392 KB |
| **Payload Files** | 1,202 files | **1,237 files** | **+35 files** |
| **Application Modules** | 76 modules | **80 modules** | **+4 new modules** |
| **Visual Templates** | 992 templates | **1,026 templates** | **+35 new templates** |
| **Decrypted Fixed Points** | 862 points | **906 points** | **+44 new points** |
| **Syntax Validation** | 100% clean | **100% clean (80/80 files)** | **0 errors** |

---

## 🚀 New Application Modules

This update introduces **4 brand new application modules** located in [`Source/`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/Recovered_Source_New_Update/Source) and showcased in [`New_Application_Modules/`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/Recovered_Source_New_Update/New_Application_Modules):

### 1. `equipment_upgrade.py`: Hero Equipment Automation
Automates the Blacksmith building interface to manage, inspect, and upgrade Hero Equipment using Shiny, Glowy, and Starry Ore.
- **Supported Heroes:** Barbarian King, Archer Queen, Minion Prince *(new hero)*, Grand Warden, Royal Champion.
- **Multi-Scale Detection:** OpenCV template matching over scales `[0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2]` with threshold `0.7`.
- **Region Scanning:**
  - `EQUIP_COMMON_REGION`: `(114, 527, 333, 748)`
  - `EQUIP_EPIC_REGION`: `(333, 528, 558, 749)`
  - `EQUIP_CURRENTLY_EQUIPPED_REGION`: `(136, 339, 1461, 444)`
- **Key Functions:**
  - `run(adb, vision, cfg, pause_if_needed=None, profile_name=None)`
  - `run_hero_priority(adb, vision, hero_settings, pause_if_needed=None)`
  - `run_currently_equipped(adb, vision, pause_if_needed=None)`

### 2. `rush_bh.py`: Builder Hall Rush Engine
Fast-tracks Builder Base progression to meet requirements for unlocking the **6th Builder (B.O.B)**.
- **Priority Upgrades:**
  - `BUILDER_HALL_KEY = 'bb_upgrade_builder_hall'`
  - `MAIN_LADDER`: Gold Storage, Elixir Storage, Star Laboratory
  - `RESEARCH_CHAIN`: Baby Dragon, Sneaky Archer, Raged Barbarian (to level 18)
  - `HERO_PRIORITY`: Battle Copter, Battle Machine (to combined level 45)
  - `LOW_PRIORITY`: Multi-Mortar (level 8 gear-up requirement)

### 3. `startup_checks.py`: Special Events & Dialogue Resolver
Runs immediately after client boot before entering the Home Village loop:
- **WWE Event & Mystery Cards:** Automatically detects `wwe_chest.png` and cards, taps through reward dialogs.
- **Return Bonus:** Identifies welcome-back rewards and claims them via `_handle_return_bonus()`.
- **Canvas Settle:** Uses `settle_until_home()` to verify the main village camera is settled.

### 4. `ranked_unlock.py`: Ranked Battle Unlocker
Automates the prerequisite dialogues and menu sequence required to unlock Ranked Battles on newly leveled accounts using `run_ranked_unlock_script()`.

---

## 📦 Complete Module Architecture (80 Modules)

```
Source/
├── pyarmor_runtime_015394/          # Native PyArmor runtime extension
├── attack/                          # 15 Combat deployment modules
│   ├── attacklogic.py, barchgob.py, dragon.py, edragon.py
│   ├── fourside_coords.py, geometry.py, sbarb.py, sminion.py
│   ├── threeside_coords.py, thrower.py, valkyrie.py, valkyrie_1side.py
│   └── war_onestar.py, war_twothreestar.py
├── builder_base/                    # 5 Builder Base automation modules
│   ├── functions.py, main.py, vision_builder.py, walls.py
├── profiles/                        # 3 Profile management modules
│   ├── config_manager.py, profile_manager.py
├── ui/                              # 10 PySide6 Qt6 UI modules
│   ├── account_creation_worker.py, activation_window.py, bot_worker.py
│   ├── gui.py, i18n.py, main_window.py, mini_window.py, stats_store.py
├── utils/                           # 4 Utility & path modules
│   ├── multitouch.py, profile_backup.py, runtime_paths.py
└── Root Application Modules (43):
    ├── equipment_upgrade.py         # [NEW] Hero equipment auto-upgrader
    ├── rush_bh.py                   # [NEW] Builder Hall rushing algorithm
    ├── startup_checks.py            # [NEW] Pre-village modal & event chest handler
    ├── ranked_unlock.py             # [NEW] Ranked battles unlock sequence
    ├── actions.py, adb.py, army_update.py, auto_place_building.py
    ├── auto_place_walls.py, bb_obstacle_removal.py, builder_boat.py
    ├── capital_raid.py, clangames.py, collect_achievements.py
    ├── control.py, create_profile.py, defaults.py, donations.py
    ├── error_popup_watcher.py, farming.py, findblacksmith.py, findcc.py
    ├── fixed_points.py, fixed_points_source.py, gui.py, license_manager.py
    ├── main.py, main_window.py, multitouch.py, obstacle_removal.py
    ├── process.py, ranked.py, recovery.py, request_and_leave.py
    ├── rush_th.py, startup.py, stats.py, ui2_zoom.py, updater_helper.py
    ├── upgrades_research.py, vision.py, walls.py, war.py, weekly_deal.py
```

---

## 🎨 New Visual Templates (35 Added)

The update adds 35 new OpenCV template assets in [`Resources/templates/`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/Recovered_Source_New_Update/Resources/templates):
- **Equipment Buttons:** `eq_upgrade_button.png`, `eq_confirm_button.png`
- **Capital Raid Spells:** `raid_graveyard.png`, `raid_heal.png`, `raid_jump.png`, `raid_rage.png`
- **Capital Raid Digits:** `digits/raid/0.png` through `digits/raid/9.png`
- **Event Troops:** `event_barcher.png`, `event_giantskeleton.png`, `event_hogwizard.png`, `event_pumpkinbarbarian.png`, `event_royalghost.png`, `event_skeletonbarrel.png`, `event_totemthrower.png`, `event_witchgolem.png`
- **Upgrades & Research:** `bb_upgrade_builder_hall.png`, `bb_upgrade_clock_tower.png`, `home_research_angry_spell.png`, `home_research_ruin_witch.png`, `ui/upgrade_weapon.png`
- **War & Events:** `start_cwl.png`, `cwl_warinfo.png`, `wwe_chest.png`, `ranked_unlocked.png`, `townhall_continue.png`

---

## 🔑 Decrypted Fixed Points (906 Total)

Decrypted using AES-256-GCM from `fixed_points_data.enc`:
- **Total Points:** **906 coordinates and regions** (+44 new points)
- Exported cleanly in [`Source/fixed_points_source.py`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/releases/v2.1-update/Source/fixed_points_source.py) with complete `__all__` list.

---

## 📁 Directory Layout

```
releases/v2.1-update/
├── README.md                        # This documentation file
├── New_Application_Modules/         # Showcase of 4 new update modules
│   ├── equipment_upgrade.py
│   ├── ranked_unlock.py
│   ├── rush_bh.py
│   ├── startup_checks.py
│   └── README.md
├── Source/                          # 80 operational Python source modules
├── Resources/                       # 1,026 templates, assets, and 11 locales
├── Config/                          # bot.config, license.key, profiles
├── Dependencies/                    # adb, tesseract, manifests
├── Metadata/                        # PE headers, section maps, sha256 hashes
├── Analysis/                        # Constants dumps, module hierarchy
└── Project/                         # run.py, test_suite.py, requirements.txt
```

---

## 🚀 Quick Start & Execution

1. **One-Click Batch Launcher:**
   Double click [`run_v2_update.bat`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/run_v2_update.bat) (or `run_bot.bat`) in the repository root.

2. **Command Line Execution:**
   ```cmd
   cd releases\v2.1-update\Source
   python ..\Project\run.py
   ```

3. **Run Test Suite:**
   ```cmd
   cd releases\v2.1-update\Project
   python test_suite.py
   ```

---

## ✅ Verification & Integrity
- All 80 Python files compile cleanly with 0 syntax errors:
  ```powershell
  python -m py_compile (Get-ChildItem -Path "releases\v2.1-update\Source" -Recurse -Filter *.py).FullName
  ```
- All 3 test cases in [`Project/test_suite.py`](file:///c:/Users/aradh/Desktop/Auto%20Clash%20clone%20Vip/releases/v2.1-update/Project/test_suite.py) pass with `OK`.
- The original executables (`binaries/v2.1-update/AutoClash.exe`) remain strictly untouched and byte-identical.
