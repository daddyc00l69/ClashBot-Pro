# -*- coding: utf-8 -*-
"""
ClashBot-Pro Application Launcher
"""
import os
import sys

# Add Source directory to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(BASE_DIR, "Source")
if SOURCE_DIR not in sys.path:
    sys.path.insert(0, SOURCE_DIR)

print("=" * 60)
print("  ClashBot-Pro - Launching Application")
print("=" * 60)
print(f"Base Directory:   {BASE_DIR}")
print(f"Source Directory: {SOURCE_DIR}")

try:
    import gui
    print("Application bootstrap succeeded.")
except ImportError as e:
    print(f"Launch Notice: {e}")
    print("Running in headless / test mode.")
