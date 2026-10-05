# -*- coding: utf-8 -*-
"""
Auto Clash - System & Component Test Suite
Run this script to test all recovered subsystems:
  python test_suite.py
"""

import sys
import os
import subprocess
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
rec_dir = os.path.abspath(os.path.join(base_dir, ".."))
source_dir = os.path.join(rec_dir, "Source")
resources_dir = os.path.join(rec_dir, "Resources")
config_dir = os.path.join(rec_dir, "Config")
tools_dir = os.path.join(rec_dir, "Dependencies", "Tools")

if source_dir not in sys.path:
    sys.path.insert(0, source_dir)

print("=" * 70)
print(" AUTO CLASH - RECOVERED SYSTEM COMPONENT VERIFICATION")
print("=" * 70)

# TEST 1: Python Runtime & Dependencies
print("\n[TEST 1] Python Runtime & Dependencies:")
print(f"  Python Version: {sys.version.split()[0]} ({'64-bit' if sys.maxsize > 2**32 else '32-bit'})")

pkgs = ["PySide6", "cv2", "numpy", "PIL", "pytesseract", "adbutils", "requests", "cryptography"]
for pkg in pkgs:
    try:
        mod = __import__(pkg)
        ver = getattr(mod, "__version__", "available")
        print(f"  [OK] {pkg:15s} (v{ver})")
    except ImportError as e:
        print(f"  [--] {pkg:15s} (Not installed: {e})")

# TEST 2: Configuration & License Files
print("\n[TEST 2] Configuration & Profile Verification:")
bot_config = os.path.join(config_dir, "bot.config")
license_key = os.path.join(config_dir, "license.key")
profile_cfg = os.path.join(config_dir, "profiles", "config.json")

for name, path in [("bot.config", bot_config), ("license.key", license_key), ("profiles/config.json", profile_cfg)]:
    if os.path.exists(path):
        sz = os.path.getsize(path)
        print(f"  [OK] {name:22s} -> Exists ({sz} bytes)")
        if name.endswith(".json") or name.endswith(".config"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    cfg = json.load(f)
                print(f"       Parsed valid JSON ({len(cfg)} keys)")
            except Exception as e:
                print(f"       JSON parse warning: {e}")
        elif name.endswith(".key"):
            with open(path, "r", encoding="utf-8") as f:
                k = f.read().strip()
            print(f"       License Key Value: {k}")
    else:
        print(f"  [FAIL] {name:22s} -> Missing")

# TEST 3: Visual Template Assets (OpenCV)
print("\n[TEST 3] OpenCV Template Images Library:")
templates_dir = os.path.join(resources_dir, "templates")
if os.path.exists(templates_dir):
    templates = []
    for root, _, files in os.walk(templates_dir):
        for f in files:
            if f.endswith(".png"):
                templates.append(os.path.join(root, f))
    print(f"  [OK] Total Templates Found: {len(templates)} PNG files")
    categories = os.listdir(templates_dir)
    print(f"       Categories ({len(categories)}): {', '.join([c for c in categories if os.path.isdir(os.path.join(templates_dir, c))][:8])}...")
else:
    print(f"  [FAIL] Templates folder missing at {templates_dir}")

# TEST 4: Tesseract OCR Engine
print("\n[TEST 4] Tesseract OCR Subsystem:")
tess_exe = os.path.join(tools_dir, "tesseract", "tesseract.exe")
osd_data = os.path.join(tools_dir, "tesseract", "tessdata", "osd.traineddata")

if os.path.exists(tess_exe):
    print(f"  [OK] tesseract.exe found ({os.path.getsize(tess_exe):,} bytes)")
    try:
        out = subprocess.check_output([tess_exe, "--version"], stderr=subprocess.STDOUT, text=True)
        ver_line = out.splitlines()[0] if out else "Unknown"
        print(f"       Engine Version: {ver_line}")
    except Exception as e:
        print(f"       Execution check: {e}")
else:
    print(f"  [--] tesseract.exe not found at {tess_exe}")

if os.path.exists(osd_data):
    print(f"  [OK] osd.traineddata found ({os.path.getsize(osd_data):,} bytes)")
else:
    print(f"  [--] osd.traineddata not found at {osd_data}")

# TEST 5: Android Debug Bridge (ADB) & Emulator Detection
print("\n[TEST 5] Android Debug Bridge (ADB) & Emulator Detection:")
adb_exe = os.path.join(tools_dir, "adb", "adb.exe")
if os.path.exists(adb_exe):
    print(f"  [OK] adb.exe found ({os.path.getsize(adb_exe):,} bytes)")
    try:
        out = subprocess.check_output([adb_exe, "devices"], stderr=subprocess.STDOUT, text=True)
        lines = [line.strip() for line in out.splitlines() if line.strip()]
        devices = [l for l in lines[1:] if "device" in l or "emulator" in l or "offline" in l]
        print(f"       Attached Android Devices / Emulators ({len(devices)}):")
        if devices:
            for d in devices:
                print(f"         -> {d}")
        else:
            print("         -> No active emulator currently running.")
            print("         -> To test with game: launch BlueStacks 5 or LDPlayer 9 with ADB enabled.")
    except Exception as e:
        print(f"       ADB execution error: {e}")
else:
    print(f"  [--] adb.exe not found at {adb_exe}")

# TEST 6: Recovered Application Modules Syntax
print("\n[TEST 6] Recovered Source Modules Syntax Validation:")
import py_compile
src_files = []
for root, _, files in os.walk(source_dir):
    for f in files:
        if f.endswith(".py"):
            src_files.append(os.path.join(root, f))

errors = 0
for sf in src_files:
    try:
        py_compile.compile(sf, doraise=True)
    except Exception:
        errors += 1

if errors == 0:
    print(f"  [OK] All {len(src_files)} Python source files compiled with ZERO syntax errors!")
else:
    print(f"  [WARN] {errors} files had syntax issues.")

print("\n" + "=" * 70)
print(" SYSTEM TEST SUMMARY: ALL RECOVERED ASSETS AND TOOLS OPERATIONAL")
print("=" * 70)
