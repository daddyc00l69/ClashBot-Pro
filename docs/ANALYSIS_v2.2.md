# In-Depth Reverse-Engineering & Architectural Audit: ACBot (v2.2.6 Update)

## 1. Executive Summary

This report provides a comprehensive technical analysis of the updated Windows executable **`ACBot.exe`** (97,394,688 bytes), released with native support for the new Clash of Clans Game UI.

Static PE inspection, resource carving, and Nuitka/PyArmor introspection verify that the application remains a **Python 3.10.11-based automation platform** compiled to native x86-64 machine code using **Nuitka**, packaged as a **Nuitka Onefile** payload, and virtualized by **PyArmor 7/8 (Runtime ID: `015394`)**.

| Attribute | Technical Value |
|---|---|
| **Binary Name** | `ACBot.exe` |
| **File Size** | 97,394,688 bytes (92.88 MB) |
| **SHA-256 Hash** | `c8628d1a8b3bdf70c0fedb9853a99668376eb03898953659b36eee8fae541dd6` |
| **MD5 Hash** | `c639968573eead13f0704d9b90dc629b` |
| **Architecture** | x86-64 / AMD64 (PE32+) |
| **Packaging** | Nuitka Onefile (Zstandard payload signature: `KAY` + `0xFD2FB528`) |
| **Core DLL (`gui.dll`)** | 94,718,464 bytes (90.33 MB) |
| **Constants & Modules Blob** | `RT_RCDATA` ID 3 (14,917,730 bytes) |
| **Application Modules** | **86 modules** (Expanded from 80 in v2.1.0) |
| **Decrypted Fixed Points** | **956 coordinate constants** (Expanded from 906 in v2.1.0) |
| **Licensing Server** | `https://api.acbot.site/validate` |
| **Active License Key** | `[REMOVED - VIP UNLOCKED / NO KEY REQUIRED]` (Valid through 2026-11-16) |

---

## 2. Binary Packaging & Extraction Details

### 2.1 The Outer Launcher: `ACBot.exe`
- **Resource `RT_RCDATA` ID 27:**
  - File offset: `0x80198` (RVA `0xae798`, size: 96,867,168 bytes).
  - Decompresses via Zstandard into 1,199 uncompressed files (314.49 MB) containing runtime dependencies, OpenCV templates, locales, and native libraries.

### 2.2 The Main Engine: `gui.dll`
- Primary entry point: Exported function `run_code`.
- **Resource `RT_RCDATA` ID 3 (`.bytecode`):**
  - Offset: `0x4DCF798`, Size: 14,917,730 bytes.
  - Houses the Nuitka module constants blob and 86 PyArmor obfuscated application bytecode chunks.

---

## 3. Inventory of Newly Added & Updated Modules

The v2.2.6 release expands the codebase from 80 to **86 application modules**:

### 3.1 `new_ui_intro.py` (New Game UI Support)
- **Role:** Handles dialogue popups, new player onboarding screens, and revised layout modals in updated Supercell game clients.
- **Key Constant:** `NEW_UI_INTRO_STEPS` (31 distinct tap/swipe actions automating intro cinematics and layout acceptance).

### 3.2 `bot_host.py` (Process Hosting Supervisor)
- **Role:** Replaces legacy process monitors with a robust emulator background supervisor. Manages multi-instance ADB binding and health pings.

### 3.3 `device_api.py` (Device Input/Output Abstraction)
- **Role:** Unified low-level device communication abstraction layer wrapping ADB, UIAutomator2, and Linux kernel touch injection.

### 3.4 `magic_items.py` (Magic Items Shop & Inventory)
- **Role:** Scans the Magic Items grid (`MAGIC_ITEMS_GRID_REGION`) and automates potion consumption (Clock Tower, Training, Builder, Resource potions).

### 3.5 `unplaced_items.py` (Building Stash & Auto-Place)
- **Role:** Resolves unplaced structures from the store/town hall upgrades, auto-stashing or placing them cleanly on the base grid.

### 3.6 `ui/update_prompt.py` (Interactive Updater Dialog)
- **Role:** Native Qt/PySide6 modal prompt notifying users of remote version releases and forced update channels.

### 3.7 `utils/screen_scale.py` (Responsive Screen Scaler)
- **Role:** Normalizes absolute screen coordinates across custom emulator resolutions (1600x900 base standard).

### 3.8 `utils/locale_safe.py` (Safe String Resolver)
- **Role:** Prevents character decoding crashes on Asian, Cyrillic, and Arabic system locales.

---

## 4. Verification & Validation Audit

All recovered source files in `Updated_Exe_Code/Source/` have been verified:
1. **Syntax Checking:** 89/89 Python files compiled with `python -m py_compile` with **0 errors**.
2. **Runtime Execution:** Tested live under Python 3.10 with `pyarmor_runtime_015394`, confirming functional imports for all modules.
3. **Decrypted Fixed Points:** Exported to `fixed_points_source.py` with 956 validated constants for seamless dual-mode execution (both offline and online).
