# -*- coding: utf-8 -*-
"""
ClashBot-Pro v2.2.6 - Main Application Launcher
Native Clash of Clans New Game UI Support Engine
VIP Unlocked - Offline Local Authentication (No Login Key Required)
"""
import sys
import os
import traceback
from datetime import datetime

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

# Setup crash logger
crash_log_file = os.path.join(root_dir, 'crash.log')
def log_unhandled_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    err_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print("\n[!] FATAL CRASH DETECTED:\n" + err_msg, file=sys.stderr, flush=True)
    try:
        with open(crash_log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*70}\nCRASH REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{'='*70}\n")
            f.write(err_msg)
    except Exception:
        pass

sys.excepthook = log_unhandled_exception

print("[*] Initializing VIP engine & license bypass...", flush=True)
import license_manager
import gui

# Hook LicenseSplash to automatically validate without prompting for login key
orig_splash_init = gui.LicenseSplash.__init__
def _unlocked_splash_init(self, *args, **kwargs):
    orig_splash_init(self, *args, **kwargs)
    res = license_manager.validate_license_details('VIP-LIFETIME-UNLOCKED')
    self._on_validation_result('VIP-LIFETIME-UNLOCKED', res)

gui.LicenseSplash.__init__ = _unlocked_splash_init

def _bypass_splash_exec(self):
    self.accept()
    return 1

gui.LicenseSplash.exec = _bypass_splash_exec
gui.LicenseSplash.exec_ = _bypass_splash_exec

# Hook ui.main_window to protect against fatal license closures or forced update exits
try:
    import ui.main_window
    ui.main_window.MainWindow.handle_fatal_license = lambda self, *args, **kwargs: print("[VIP Hook] Ignored license recheck error")
    ui.main_window.ask_forced_update_choice = lambda *args, **kwargs: False
    ui.main_window.launch_self_update = lambda *args, **kwargs: False
except Exception as e:
    print(f"[!] Warning hooking ui.main_window: {e}")

print("[+] Launching ClashBot-Pro window...", flush=True)

if __name__ == '__main__':
    try:
        gui.run()
    except Exception as e:
        log_unhandled_exception(*sys.exc_info())
        input("\nPress Enter to exit...")
