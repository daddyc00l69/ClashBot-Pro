# -*- coding: utf-8 -*-
"""
ClashBot-Pro v2.2.6 - Main Application Launcher
Native Clash of Clans New Game UI Support Engine
VIP Unlocked - Offline Local Authentication (No Login Key Required)
"""
import sys
import os

print("[*] Starting ClashBot-Pro v2.2.6...", flush=True)

# Set working directory and path resolution
root_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(root_dir)

src_dir = os.path.join(root_dir, 'Source')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Ensure runtime tools & resources are discoverable
tools_adb = os.path.join(root_dir, 'Tools', 'adb')
if os.path.exists(tools_adb):
    os.environ['PATH'] = tools_adb + os.pathsep + os.environ.get('PATH', '')

print("[*] Initializing VIP engine & license bypass...", flush=True)
import license_manager
import gui

# Hook LicenseSplash to automatically validate without prompting for login key
orig_splash_init = gui.LicenseSplash.__init__
def _unlocked_splash_init(self, *args, **kwargs):
    orig_splash_init(self, *args, **kwargs)
    res = license_manager.validate_license_details('VIP_UNLOCKED')
    self._on_validation_result('VIP_UNLOCKED', res)

gui.LicenseSplash.__init__ = _unlocked_splash_init

def _bypass_splash_exec(self):
    res = license_manager.validate_license_details('VIP_UNLOCKED')
    self._on_validation_result('VIP_UNLOCKED', res)
    return 1

gui.LicenseSplash.exec = _bypass_splash_exec
gui.LicenseSplash.exec_ = _bypass_splash_exec

print("[+] Launching ClashBot-Pro window...", flush=True)

if __name__ == '__main__':
    gui.run()
