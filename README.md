<div align="center">

# ⚔️ ClashBot-Pro

### *Next-Generation Autonomous Automation & Intelligence Suite for Clash of Clans*

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-PySide6%20%2F%20Qt6-41CD52.svg?logo=qt&logoColor=white)](https://www.qt.io/)
[![Vision](https://img.shields.io/badge/Vision-OpenCV%20%26%20Tesseract-5C3EE8.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011%20(64--bit)-0078D6.svg?logo=windows&logoColor=white)](https://microsoft.com/windows)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-AradhyeTushar-ff69b4.svg?logo=github&logoColor=white)](https://github.com/AradhyeTushar)
[![Repository](https://img.shields.io/badge/GitHub-ClashBot--Pro-181717.svg?logo=github&logoColor=white)](https://github.com/AradhyeTushar/ClashBot-Pro)

<p align="center">
  <b>High-performance desktop automation suite featuring OpenCV visual pattern matching, OCR resource parsing, intelligent troop deployment mechanics, Clan War coordination, and multi-village management.</b>
</p>

---

</div>

## 📑 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Directory Structure](#-directory-structure)
- [Prerequisites](#-prerequisites)
- [Quick Start & Installation](#-quick-start--installation)
- [Emulator Configuration](#-emulator-configuration)
- [Configuration & Profiles](#-configuration--profiles)
- [Localization](#-localization)
- [Author & Credits](#-author--credits)
- [Disclaimer & License](#-disclaimer--license)

---

## 🌟 Overview

**ClashBot-Pro** is a reverse-engineered, reconstructed Python 3.10 and PySide6 (Qt 6) automation architecture engineered for complete autonomous lifecycle management in *Clash of Clans*. 

The system operates externally through Android Debug Bridge (`ADB`) and screen capture technologies—ensuring native client integrity without direct in-memory manipulation. It integrates 990+ high-precision computer vision templates, hardware-accelerated OCR, and adaptive battle state machines to deliver an enterprise-grade automation platform.

---

## ⚡ Key Features

### 🏹 1. Intelligent Combat & Farming Engine
- **Target Filtering:** Automated multiplayer search evaluating live Gold, Elixir, Dark Elixir, and Town Hall thresholds.
- **Dynamic Deployment Algorithms:**
  - *Barch & Goblins (`barchgob.py`):* Perimeter collector farming with minimal troop expenditure.
  - *Sneaky Goblins & Sneaky Minions (`sbarb.py`, `sminion.py`):* Surgical resource sniping behind walls.
  - *Dragon & Electro Dragon Assault (`dragon.py`, `edragon.py`):* Funnel creation and chain-lightning path optimization.
  - *Valkyrie Funneling (`valkyrie.py`, `valkyrie_1side.py`):* Concentrated core penetration.
  - *Siege Machines & Throwers (`thrower.py`):* Wall-busting line deployment.
- **Smart Surrender:** Automatic battle exit upon achieving target resource collection or star objectives.

### 🏰 2. Clan Operations & War Management
- **Clan Castle Requests & Donations (`donations.py`):** Chat monitor detecting troop/spell requests with automated donation fulfillment.
- **Request & Leave (`request_and_leave.py`):** High-speed clan-hopping loop for rapid XP and badge boosting.
- **Clan Games Task Picker (`clangames.py`):** Automated challenge selection, execution, and reward claiming.
- **Clan Capital Raids (`capital_raid.py`):** Weekend raid assault participation and medal optimization.
- **Clan War Engine (`war.py`):** Strategy-based target assignment (Safe 1-Star or Optimized 3-Star attacks).

### 🛠️ 3. Village Progression & Resource Automation
- **Wall Upgrade System (`walls.py`, `auto_place_walls.py`):** Automatic excess Gold/Elixir dumping into wall levels.
- **Obstacle Clearing (`obstacle_removal.py`, `bb_obstacle_removal.py`):** Automatic gem harvesting from trees, bushes, and gem boxes.
- **Building Upgrades & Research (`upgrades_research.py`, `rush_th.py`):** Continuous laboratory research and idle builder allocation.
- **Trader & Weekly Deals (`weekly_deal.py`):** Automated trader shop reward claiming and free item redemption.

### 🌙 4. Builder Base Subsystem (`builder_base/`)
- **Clock Tower Boost:** Scheduled daily activation to accelerate production.
- **Automated Battles:** Auto-deployment of Baby Dragons/Barbs for star bonuses.
- **Gem Mine & Cart Collector:** Continuous passive resource harvesting.

### 👁️ 5. Vision & Optical Intelligence
- **OpenCV Pattern Recognition (`vision.py`):** 992+ indexed game templates across all resolutions.
- **OCR Timer & Resource Recognition:** Tesseract-powered reading of countdown timers, shield remaining, and upgrade costs.
- **Pinch-to-Zoom Calibration (`ui2_zoom.py`):** Automatic zoom resets and anchor realignment upon village load.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[PySide6 UI Dashboard] -->|Signals / Controls| B[BotWorker Thread]
    B --> C[ADB Bridge / Screencap Engine]
    B --> D[Computer Vision & OCR Engine]
    B --> E[Battle State Machine]
    
    C -->|Touch Gestures / ADB Commands| F[Android Emulator: BlueStacks / LDPlayer]
    F -->|Raw Frame Buffer| D
    
    D -->|Template Coordinates / OCR Data| E
    E -->|Deployment Decisions| C
    
    B --> G[Config & Profile Manager]
    G --> H[JSON Profile Storage]
```

---

## 📁 Directory Structure

```text
ClashBot-Pro/
├── Recovered_Source/
│   ├── Source/                           # Application source code
│   │   ├── attack/                       # Combat deployment scripts & coordinates
│   │   │   ├── attacklogic.py            # Battle state machine & sequencing
│   │   │   ├── barchgob.py               # Barbarian / Archer / Goblin strategy
│   │   │   ├── dragon.py                 # Dragon assault automation
│   │   │   ├── edragon.py                # Electro Dragon chain-lightning logic
│   │   │   ├── geometry.py               # Screen tile mathematics & coordinates
│   │   │   └── war_twothreestar.py       # War strategy planner
│   │   ├── builder_base/                 # Builder Base subsystem
│   │   │   ├── functions.py              # Clock tower, gem mine, cart collection
│   │   │   └── main.py                   # Builder Base loop orchestrator
│   │   ├── profiles/                     # Multi-village profile & config management
│   │   ├── ui/                           # PySide6 (Qt6) GUI application
│   │   │   ├── main_window.py            # Main application dashboard
│   │   │   ├── mini_window.py            # Compact floating overlay widget
│   │   │   └── bot_worker.py             # Asynchronous bot execution thread
│   │   ├── utils/                        # Runtime helpers & multitouch generators
│   │   ├── adb.py                        # ADB socket communication bridge
│   │   ├── farming.py                    # Multiplayer search & loot evaluation
│   │   ├── vision.py                     # OpenCV template matching & OCR engine
│   │   └── walls.py                      # Automatic wall upgrade engine
│   ├── Resources/
│   │   ├── assets/                       # UI icons, stylesheets, and branding
│   │   ├── templates/                    # 992 OpenCV visual template images
│   │   └── locales/                      # Multi-language translation packs (.json)
│   ├── Config/
│   │   └── profiles/                     # User village configurations
│   ├── Dependencies/
│   │   ├── Tools/                        # Embedded adb & tesseract binaries
│   │   └── requirements.txt              # Production Python package manifest
│   ├── Metadata/                         # Binary analysis, PE headers, and hashes
│   └── Project/
│       ├── run.py                        # Python application entry point
│       └── setup_env.bat                 # Virtual environment bootstrap script
├── .gitignore                            # Standard Git ignore rules
├── ANALYSIS.md                           # In-depth reverse engineering documentation
├── DEPENDENCIES.md                       # Comprehensive toolchain and package audit
├── RECOVERY_REPORT.md                    # Verification and decompilation report
├── README.md                             # Project documentation (this file)
└── run_bot.bat                           # 1-Click portable launcher
```

---

## 💻 Prerequisites

- **Operating System:** Windows 10 or Windows 11 (64-bit)
- **Python Version:** Python 3.10.x 64-bit ([Python 3.10.11](https://www.python.org/downloads/release/python-31011/) recommended)
- **Android Emulator:** 
  - [BlueStacks 5](https://www.bluestacks.com/) (Nougat 64-bit / Pie 64-bit)
  - [LDPlayer 9](https://www.ldplayer.net/)
- **ADB Debugging:** Enabled in emulator settings.

---

## 🚀 Quick Start & Installation

### Option 1: Automated 1-Click Setup (Recommended)

1. Clone or download the repository:
   ```bash
   git clone https://github.com/AradhyeTushar/ClashBot-Pro.git
   cd ClashBot-Pro
   ```
2. Double-click **`run_bot.bat`** or run:
   ```cmd
   .\run_bot.bat
   ```
   *The launcher automatically resolves all local project paths and boots the GUI.*

---

### Option 2: Manual Setup

1. **Navigate to the Project directory:**
   ```bash
   cd Recovered_Source/Project
   ```

2. **Create and activate a virtual environment:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```cmd
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```cmd
   python run.py
   ```

---

## 📱 Emulator Configuration

For pixel-perfect template matching, configure your emulator with the following settings:

| Setting | Recommended Value |
|---|---|
| **Display Resolution** | `860 x 480` or `1280 x 720` (Landscape) |
| **Pixel Density (DPI)** | `160 DPI` |
| **Graphics Engine** | DirectX or OpenGL with GPU Rendering |
| **ADB Debugging** | Enabled (Default Port: `5555` / `5556`) |

---

## 🌐 Localization

The interface supports 11 languages with hot-swapping via the GUI:

| Code | Language | Code | Language |
|:---:|:---|:---:|:---|
| `en` | English | `hi` | हिन्दी (Hindi) |
| `es` | Español (Spanish) | `fr` | Français (French) |
| `de` | Deutsch (German) | `ru` | Русский (Russian) |
| `ar` | العربية (Arabic) | `id` | Bahasa Indonesia |
| `pt-br` | Português (Brasil) | `tl` | Tagalog (Filipino) |
| `tr` | Türkçe (Turkish) | | |

---

## 👤 Author & Maintainer

Maintained and developed by:

**Aradhye Tushar**  
- **GitHub:** [@AradhyeTushar](https://github.com/AradhyeTushar)  
- **Repository:** [ClashBot-Pro](https://github.com/AradhyeTushar/ClashBot-Pro)

---

## ⚖️ Disclaimer & License

> [!IMPORTANT]
> **Educational & Research Notice:** This project is intended strictly for educational, security research, and interoperability analysis purposes. Clash of Clans is a registered trademark of Supercell Oy. This project is not affiliated with, endorsed, sponsored, or specifically approved by Supercell. Users are responsible for complying with the game's Terms of Service.
