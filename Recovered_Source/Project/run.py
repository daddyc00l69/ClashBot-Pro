# -*- coding: utf-8 -*-
"""
Auto Clash - Recovered Source Project Launcher
Launches the full GUI application directly from the decompiled & recovered source code.
"""
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.abspath(os.path.join(current_dir, "..", "Source"))
if source_dir not in sys.path:
    sys.path.insert(0, source_dir)

# Set working directory to Source to ensure local resource paths resolve accurately
os.chdir(source_dir)

if __name__ == "__main__":
    print("[*] Launching Auto Clash GUI from recovered Python source...")
    from ui import gui
    sys.exit(gui.run())
