# Clash Bot AI v2.2.7 - Clash of Clans Automation Engine

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31011/)
[![Status](https://img.shields.io/badge/status-VIP%20Unlocked%20(Offline%20Mode)-success.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-lightgrey.svg)]()

A standalone, fully configured Python automation engine for **Clash of Clans** (**Clash Bot AI** version 2.2.7). Extracted and reconstructed from the original executable package with offline VIP lifetime authorization enabled.

---

## 🌟 Key Features

- **Automated Base Farming:** Smart gold, elixir, and dark elixir collection and troop deployment.
- **Builder Base 2.0:** Automated Builder Base attacks, star bonus farming, and resource collector management.
- **Clan Games & Clan Capital:** Smart challenge selection and raid weekend attacks with custom troop/spell compositions.
- **War & CWL:** Configurable attack strategies, target selection, and Clan Castle donation requests.
- **Multi-Account & Profiles:** Independent configuration profiles with automatic emulator switching.
- **Computer Vision & OCR:** Integrated OpenCV template matching (113 template categories) and embedded Tesseract OCR for text recognition.
- **VIP Offline Lifetime:** Cloud license dependency bypassed; operates indefinitely offline without server authentication.

---

## 📂 Project Structure

```text
Clash Bot AI v2.2.7/
├── run_bot.bat                 # One-click Windows batch launcher
├── run_bot.py                  # Main Python application entry point
├── bot.config                  # Bot configuration settings
│
├── Source/                     # Python core modules & runtime
│   ├── ui/                     # PySide6 GUI interface & widgets
│   ├── fixed_points.py         # 1,009 exact UI pixel coordinates & crop engine
│   ├── license_manager.py      # Offline lifetime VIP authorization handler
│   ├── pyarmor_runtime_015394/ # PyArmor bytecode security runtime
│   └── ...                     # Automation workers, vision, attack logic
│
├── templates/                  # 113+ OpenCV computer vision template match sets
├── assets/                     # Application icons, fonts, and coordinate assets
│
└── Tools/                      # Embedded runtime tools
    ├── adb/                    # Android Debug Bridge (ADB) binaries
    └── tesseract/              # Tesseract OCR engine binaries & language data
```

---

## 🚀 Quick Start

### Prerequisites
1. **Python 3.10 (64-bit):**
   - Download and install Python 3.10 from [python.org](https://www.python.org/).
   - Ensure you check **"Add Python to PATH"** during installation.

2. **Install Required Python Dependencies:**
   Open a terminal/cmd window and run:
   ```bash
   pip install PySide6 opencv-python numpy cryptography psutil pytesseract adbutils
   ```

3. **Android Emulator:**
   - Any modern Android emulator (BlueStacks, LDPlayer, MEmu, Nox, etc.) configured with ADB enabled.

---

### Running the Bot

#### Method 1: Batch Launcher (Recommended)
Double-click:
```cmd
run_bot.bat
```
The script will automatically detect your Python 3.10 installation and start the bot with safety pause guards enabled.

#### Method 2: Command Line
```cmd
python run_bot.py
```

---

## 🛠️ Upgrading to Newer Bot Versions

When a new version of the bot is released (e.g., `v2.2.8`+):

1. **Unpack Executable:**
   - Extract the Nuitka payload container (`KAY` header) from the new `.exe`.
   - Update `templates/` and `assets/`.
2. **Module Extraction:**
   - Carve the compiled Python modules from `gui.dll` (Resource ID 3) into `Source/`.
   - Decrypt `assets/fixed_points_data.enc` using the AES key found in `license_manager.py` into `Source/fixed_points.py`.
   - Ensure package `__init__.py` files exist for `utils`, `ui`, `attack`, `builder_base`, and `profiles`.
3. **VIP Offline Bypass:**
   - Update `license_manager.py` to return `valid: True` and supply `_AES_KEY_B64` offline.
4. **Launch:**
   - Run via `run_bot.bat`.

---

## ⚠️ Disclaimer

This project is for educational and archival purposes only. Clash of Clans is a registered trademark of Supercell. Automation software may violate Supercell's Terms of Service; use responsibly and at your own discretion.
