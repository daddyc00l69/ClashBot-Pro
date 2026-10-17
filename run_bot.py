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

# 1. Suppress noisy Qt QThreadStorage warnings
os.environ["QT_LOGGING_RULES"] = "qt.core.qthreadstorage.warning=false;qt.qpa.*=false"

print("[*] Starting ClashBot-Pro v2.2.6...", flush=True)

# 2. Set working directory and path resolution
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

# 3. Setup crash logger
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

# 4. Hook LicenseSplash to automatically validate without prompting for login key
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

# 5. Hook ui.main_window to protect against fatal license closures or forced update exits
try:
    import ui.main_window
    ui.main_window.MainWindow.handle_fatal_license = lambda self, *args, **kwargs: print("[VIP Hook] Ignored license recheck error")
    ui.main_window.ask_forced_update_choice = lambda *args, **kwargs: False
    ui.main_window.launch_self_update = lambda *args, **kwargs: False
except Exception as e:
    print(f"[!] Warning hooking ui.main_window: {e}")

# 6. Enhance Recovery & Village Detection for New Game UI and slow PCs
try:
    import recovery
    recovery.ARMY_BUTTON_WAIT_SECONDS = 75
    print("[+] Configured recovery wait timeout: 75s")
except Exception as e:
    print(f"[!] Warning hooking recovery: {e}")

try:
    import vision
    import cv2
    import numpy as np

    orig_find_army_button = vision.Vision.find_army_button

    def _smart_find_army_button(self, *args, **kwargs):
        # 1. Try original match first
        try:
            res = orig_find_army_button(self, *args, **kwargs)
            if res:
                return res
        except Exception:
            pass

        # 2. Grab current frame
        img = self.grab()
        if img is None:
            return None

        # Convert to grayscale
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img

        # 3. Relaxed army_button match (threshold 0.68 instead of 0.90)
        tmpl_data = self.templates.get('army_button')
        if tmpl_data and 'img' in tmpl_data:
            t_img = tmpl_data['img']
            if len(t_img.shape) == 3 and t_img.shape[2] == 4:
                t_gray = cv2.cvtColor(t_img, cv2.COLOR_BGRA2GRAY)
            elif len(t_img.shape) == 3:
                t_gray = cv2.cvtColor(t_img, cv2.COLOR_BGR2GRAY)
            else:
                t_gray = t_img
            
            crop_gray = gray[300:895, 0:800]
            if crop_gray.shape[0] >= t_gray.shape[0] and crop_gray.shape[1] >= t_gray.shape[1]:
                res_mat = cv2.matchTemplate(crop_gray, t_gray, cv2.TM_CCOEFF_NORMED)
                _, max_v, _, max_l = cv2.minMaxLoc(res_mat)
                if max_v >= 0.68:
                    return (max_l[0] + tmpl_data['w'] // 2, 300 + max_l[1] + tmpl_data['h'] // 2)

        # 4. Check attack_button (always at bottom-left on Home Village)
        atk_data = self.templates.get('attack_button')
        if atk_data and 'img' in atk_data:
            t_img = atk_data['img']
            t_gray = cv2.cvtColor(t_img, cv2.COLOR_BGRA2GRAY) if (len(t_img.shape) == 3 and t_img.shape[2] == 4) else (cv2.cvtColor(t_img, cv2.COLOR_BGR2GRAY) if len(t_img.shape) == 3 else t_img)
            crop_atk = gray[650:900, 0:400]
            if crop_atk.shape[0] >= t_gray.shape[0] and crop_atk.shape[1] >= t_gray.shape[1]:
                res_mat = cv2.matchTemplate(crop_atk, t_gray, cv2.TM_CCOEFF_NORMED)
                _, max_v, _, max_l = cv2.minMaxLoc(res_mat)
                if max_v >= 0.65:
                    print(f"[Vision] Detected Home Village via Attack Button (score: {max_v:.2f})")
                    return (215, 843)

        # 5. Check shop_button (bottom-right on Home Village)
        shop_data = self.templates.get('shop_button')
        if shop_data and 'img' in shop_data:
            t_img = shop_data['img']
            t_gray = cv2.cvtColor(t_img, cv2.COLOR_BGRA2GRAY) if (len(t_img.shape) == 3 and t_img.shape[2] == 4) else (cv2.cvtColor(t_img, cv2.COLOR_BGR2GRAY) if len(t_img.shape) == 3 else t_img)
            crop_shop = gray[700:900, 1300:1600]
            if crop_shop.shape[0] >= t_gray.shape[0] and crop_shop.shape[1] >= t_gray.shape[1]:
                res_mat = cv2.matchTemplate(crop_shop, t_gray, cv2.TM_CCOEFF_NORMED)
                _, max_v, _, _ = cv2.minMaxLoc(res_mat)
                if max_v >= 0.65:
                    print(f"[Vision] Detected Home Village via Shop Button (score: {max_v:.2f})")
                    return (215, 843)

        # 6. Check if New UI intro/tutorial is on screen and tap through it
        try:
            import new_ui_intro
            new_ui_intro.run_new_ui_intro_if_present()
        except Exception:
            pass

        return None

    vision.Vision.find_army_button = _smart_find_army_button
    print("[+] Enabled Smart Home Village & New Game UI Detection")
except Exception as e:
    print(f"[!] Warning hooking vision: {e}")

# 7. Auto-save screenshot when home village is not found before relaunching
try:
    import adb
    orig_force_stop = adb.force_stop
    def _debug_force_stop(pkg, *args, **kwargs):
        if pkg == "com.supercell.clashofclans":
            try:
                screen = adb.screenshot()
                if screen is not None:
                    import cv2
                    shot_path = os.path.join(root_dir, 'failed_village_screen.png')
                    cv2.imwrite(shot_path, screen)
                    print(f"[Debug] Saved emulator screen capture to: failed_village_screen.png")
            except Exception:
                pass
        return orig_force_stop(pkg, *args, **kwargs)
    adb.force_stop = _debug_force_stop
except Exception as e:
    print(f"[!] Warning hooking adb: {e}")

print("[+] Launching ClashBot-Pro window...", flush=True)

if __name__ == '__main__':
    try:
        gui.run()
    except Exception as e:
        log_unhandled_exception(*sys.exc_info())
        input("\nPress Enter to exit...")
