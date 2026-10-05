# In-Depth Reverse-Engineering & Architectural Analysis: ClashBot-Pro

## 1. Executive Summary

This report provides a comprehensive technical analysis of the Windows executable **ClashBot-Pro** (`ClashBot-Pro Application Engine`, 97,402,368 bytes).

Through static analysis, PE header inspection, resource carving, and Nuitka/PyArmor introspection, the application has been determined to be a **Python 3.10-based automation platform** compiled to native x86-64 machine code using **Nuitka**, packaged as a **Nuitka Onefile** self-extracting payload, and protected by **PyArmor 7/8**.

| Attribute | Technical Value |
|---|---|
| **Binary Name** | `ClashBot-Pro Application Engine` |
| **File Size** | 97,402,368 bytes (92.89 MB) |
| **Architecture** | x86-64 / AMD64 (Machine `0x8664`, PE32+) |
| **Subsystem** | Windows GUI (Subsystem 2) |
| **Compiler / Toolchain** | Nuitka (Kay Hayen) v1.8 - 2.x / 4.x Compatible |
| **Onefile Compression** | Zstandard (Magic: `KAY` + `0xFD2FB528`) |
| **Embedded Payload Size** | 314.43 MB uncompressed (1,202 files) |
| **Core Native Module** | `gui.dll` (94,558,208 bytes, 90.18 MB) |
| **Python Runtime** | CPython 3.10.11 AMD64 (`python310.dll`) |
| **GUI Framework** | PySide6 6.11.2 (Qt 6.x) |
| **Obfuscation** | PyArmor 7/8 (Runtime ID `015394`) + Encrypted Assets |
| **Module Inventory** | 876 total modules in blob (76 application modules) |

---

## 2. Executable Packaging & Binary Architecture

### 2.1 The Outer Launcher: `ClashBot-Pro Application Engine`
The outer executable `ClashBot-Pro Application Engine` is a Nuitka Onefile bootstrap binary whose primary responsibility is to decompress and mount the standalone Python application environment into a transient directory at runtime.

The PE structure of `ClashBot-Pro Application Engine` contains 12 sections:
- `.text` (Raw Size: `0x1F600`): Bootstrap extraction C runtime code.
- `.data`, `.rdata`, `.pdata`, `.xdata`: Standard C runtime and exception unwind tables.
- `.rsrc` (Raw Size: `0x5CBE200` = 97,247,744 bytes): Houses the entire application payload.

#### Carved Resource: `RT_RCDATA` ID 27
Located at RVA `0xAE750` (file offset `0x80150`, size 96,875,472 bytes):
- **Magic Header:** `4B 41 59 28 B5 2F FD` (`KAY` followed by Zstandard frame magic `0xFD2FB528`).
- **Decompression:** Decompresses into a continuous stream of serialized files. Each file entry consists of:
  1. File relative path as a null-terminated UTF-16LE string.
  2. 8-byte unsigned integer (little-endian) representing uncompressed file size.
  3. Raw byte payload of the file.

### 2.2 The Inner Application DLL: `gui.dll`
Once unpacked, the primary execution engine is `gui.dll` (94.56 MB).
- Machine: x86-64.
- Exports: Exactly 1 function: `run_code`.
- Sections:
  - `.text`: `0x4A2BC00` bytes (74.17 MB of compiled native machine code).
  - `.rsrc`: `0xE75600` bytes (14.45 MB of resources).
- **Resource `RT_RCDATA` ID 3 (`.bytecode`):**
  - Offset: `0x4C10D50`, Size: 14,788,499 bytes.
  - Header: CRC32 `0xA06EA24D`, Declared Size: 14,788,491 bytes.
  - Contains Nuitka's **Constants and Modules Blob** (876 modules).

---

## 3. Module Hierarchy & Nuitka Module Table

At virtual address `0x34F5453C0`, `gui.dll` maintains Nuitka's internal module registry containing **865 registered modules**:
- **BYTECODE (601 modules):** Standard library and utility scripts stored as marshalled Python code objects inside the `.bytecode` chunk.
- **TRANSLATED / COMPILED (254 modules):** Modules translated by Nuitka into native C functions. Their Python bytecodes were eliminated during compilation; logic exists directly as x86-64 machine instructions in `.text`.
- **EXTENSION (10 modules):** Built-in native CPython extension hooks.

### Application Modules Breakdown (76 Total)
The application code consists of 76 distinct modules organized into 5 packages and root scripts:

```
[Core & Entry]
  __main__ / gui.py       : Application bootstrap & main event loop
  startup.py              : Pre-flight checks, environment verification, auto-updater
  process.py              : BlueStacks / LDPlayer process monitor
  defaults.py             : Configuration keys, defaults, and challenge dictionaries
  recovery.py             : Crash detection and emulator re-synchronization
  updater_helper.py       : Remote version comparison and binary updater

[User Interface - ui/]
  ui/__init__.py          : UI package declaration
  ui/gui.py               : QApplication initialization and dark theme styling
  ui/main_window.py       : Main dashboard, tab navigation, and settings forms
  ui/mini_window.py       : Compact floating overlay window
  ui/activation_window.py : License key entry, HWID display, and activation validation
  ui/bot_worker.py        : Worker QThread coordinating combat and village loops
  ui/account_creation_worker.py : Supercell ID automated account creation thread
  ui/stats_store.py       : In-memory session stats (Gold, Elixir, Dark, Trophies)
  ui/i18n.py              : Multi-language string resolver (11 JSON locale files)
  ui2_zoom.py             : Pinch-to-zoom screen calibration helper

[Licensing & Configuration]
  license_manager.py      : HWID generation (CPU/Motherboard UUID), license validation
  profiles/__init__.py    : Profiles package declaration
  profiles/config_manager.py : JSON configuration persistence & schema validation
  profiles/profile_manager.py: Multi-village profile switcher & slot manager

[Vision & Device I/O]
  vision.py               : OpenCV template matching (992 templates), OCR text recognition
  fixed_points.py         : Absolute screen coordinates, button anchors, UI bounds
  adb.py                  : Android Debug Bridge connector, socket pool (port 5556/5555)
  actions.py              : Touch tap, swipe, long-press, and drag-and-drop primitives
  multitouch.py           : Multi-finger coordinate stream generator
  utils/multitouch.py     : Android `/dev/input/event` multitouch driver
  utils/runtime_paths.py  : Onefile / standalone path resolver

[Combat & Raid Automation - attack/]
  attack/__init__.py      : Attack package declaration
  attack/attacklogic.py   : Combat state machine, troop deployment sequencer
  attack/geometry.py      : Isometric village tile math and perimeter offsets
  attack/fourside_coords.py: 4-quadrant edge deployment coordinates
  attack/threeside_coords.py: 3-quadrant perimeter deployment coordinates
  attack/barchgob.py      : Barbarian, Archer, and Goblin deployment
  attack/sbarb.py         : Sneaky Barbarian targeted resource sniping
  attack/sminion.py       : Sneaky Minion air defense bypass tactics
  attack/dragon.py        : Mass Dragon raid deployment logic
  attack/edragon.py       : Electro Dragon chain-lightning attack logic
  attack/valkyrie.py      : Valkyrie core rush tactics
  attack/valkyrie_1side.py: Single-side funnel Valkyrie assault
  attack/thrower.py       : Siege engine and ranged thrower tactics
  attack/war_onestar.py   : Safe 50% / 1-star Clan War strategy
  attack/war_twothreestar.py : Town Hall sniping & 3-star Clan War strategy

[Feature Modules]
  farming.py              : Multiplayer search loop, loot thresholds, next-base logic
  donations.py            : Clan chat watcher, donation requests & filling
  request_and_leave.py    : Automated clan-hopping troop requester
  clan_games.py / clangames.py: Clan Games challenge selector & progress tracker
  war.py                  : Clan War interface reader & attack scheduler
  capital_raid.py         : Clan Capital raid planner & attack executor
  walls.py                : Wall segment scanner & excess resource dumper
  upgrades_research.py    : Laboratory research manager & building upgrade assigner
  obstacle_removal.py     : Home Village obstacle cleaner
  bb_obstacle_removal.py  : Builder Base obstacle cleaner
  builder_base/functions.py: Clock Tower booster, Gem Mine, resource collector
  builder_base/main.py    : Builder Base battle loop and Baby Dragon attacks
  builder_base/vision_builder.py: Builder Base template matcher
  builder_base/walls.py   : Builder Base wall upgrade manager
  builder_boat.py         : Village transition via boat dock
  rush_th.py              : Fast Town Hall progression optimizer
  ranked.py               : Trophy pushing & competitive attack runner
  weekly_deal.py          : Trader shop item redeemer & weekly raid medals
  collect_achievements.py : Gem achievement collector
  error_popup_watcher.py  : In-game dialog, disconnect, and maintenance dismisser
  stats.py                : Statistical aggregation and run timers
```

---

## 4. Multi-Layer Obfuscation & Protection Analysis

The application incorporates a defense-in-depth protection scheme combining native compilation, bytecode encryption, and asset enciphering.

```
+-------------------------------------------------------------------+
| ClashBot-Pro Application Engine (PE32+ x86-64 Nuitka Onefile Bootstrap)             |
|   |-- RT_RCDATA ID 27 (Zstandard Compressed Archive, KAY signature)|
+-------------------------------------------------------------------+
                                  |
                                  v Decompresses at Runtime
+-------------------------------------------------------------------+
| Standalone Runtime Environment:                                   |
|   |-- python310.dll (CPython 3.10 Runtime)                        |
|   |-- PySide6 / Qt6 DLLs                                          |
|   |-- pyarmor_runtime_015394/pyarmor_runtime.pyd                  |
|   |-- gui.dll (Main Binary, 94.56 MB)                             |
|         |-- .text (Native C Machine Code for 254 modules)         |
|         |-- RT_RCDATA ID 3 (.bytecode Constants & Modules Blob)   |
|               |-- 76 Modules protected with PyArmor (PY015394)    |
+-------------------------------------------------------------------+
```

### 4.1 Layer 1: Nuitka C-Level Compilation
Nuitka parses Python abstract syntax trees (AST) and generates equivalent C code calling CPython C-API functions (`PyObject_Call`, `PyDict_GetItem`, etc.). When compiled with MinGW/MSVC, standard Python bytecode disappears from `.pyc` files, leaving native machine instructions.

### 4.2 Layer 2: PyArmor 7/8 Bytecode Protection
Before Nuitka compiled the project, the developer passed the Python codebase through **PyArmor** (Runtime `pyarmor_runtime_015394`).
- Each module was wrapped in a PyArmor bootstrap container:
  ```python
  from pyarmor_runtime_015394 import __pyarmor__
  __pyarmor__(__name__, __file__, b'PY015394...', 2)
  ```
- **Payload Header Format:**
  - Bytes 0–7: Signature `PY015394`
  - Bytes 8–11: Python version tag (`0x00 0x03 0x0A 0x00` -> Python 3.10)
  - Bytes 28–31: Header length (little-endian uint32, `0x40` = 64 bytes)
  - Bytes 32–35: Data length (little-endian uint32)
- At runtime, `pyarmor_runtime.pyd` hooks code object execution using `C_ENTER_CO_OBJECT_INDEX`, dynamically restoring opcodes into memory during function invocation.

### 4.3 Layer 3: Encrypted Asset Storage (`fixed_points_data.enc`)
Located in `Resources/assets/fixed_points_data.enc` (45,860 bytes):
- Encrypted screen calibration coordinate tables used by `fixed_points.py` and `actions.py`.
- Decrypted dynamically at startup using cryptographic routines in `license_manager.py` / `cryptography`.

---

## 5. Licensing & Activation System

The licensing subsystem is managed by `license_manager.py` and `ui/activation_window.py`.

### 5.1 Client License Key Format
The client key adheres to a standard 25-character hyphenated uppercase alphanumeric format:
```text
AC-XXXXX-XXXXX-XXXXX-XXXXX
```
For example, the bundled trial key in `Config/license.key` is:
```text
AC-2TD3B-JY2IS-5OTOD-KOTJU
```

### 5.2 Hardware Identifier (HWID)
The licensing engine computes a persistent hardware hash combining:
1. Motherboard Serial Number / UUID via Windows Management Instrumentation (`wmic baseboard get serialnumber`).
2. CPU Processor ID via `wmic cpu get processorid`.
3. Windows Machine GUID from `HKLM\SOFTWARE\Microsoft\Cryptography\MachineGuid`.
The combined string is hashed with SHA-256 and formatted for server validation.

---

## 6. Android Emulator Automation Architecture

ClashBot-Pro is designed to interface with Android emulators through ADB:
- **Default Emulators:** BlueStacks 5 (`bluestacks:custom`), LDPlayer 9 (`ldplayer`), or any generic ADB device.
- **Connection Transport:** TCP loopback connection to `127.0.0.1:5556` (BlueStacks) or `127.0.0.1:5555` (LDPlayer).
- **Control Interface:**
  1. `adbutils`: Fast socket-level screencapping (`adb exec-out screencap -p`).
  2. `uiautomator2`: Background Android daemon deployed to emulator (`app-uiautomator.apk`) for high-frequency touch injection.
  3. Custom Linux kernel input event driver (`/dev/input/event*`) for sub-millisecond multi-touch gestures (e.g. 4-finger simultaneous troop deployment).
