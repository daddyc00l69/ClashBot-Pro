# -*- coding: utf-8 -*-
"""
Clash Bot AI v2.2.7 - Application Launcher
Extracted and configured directly from executable (v2.2.7)
Offline Lifetime VIP Authorization Enabled
"""
import sys
import os
import traceback
from datetime import datetime

# 1. Suppress noisy Qt QThreadStorage / QPA warnings
os.environ["QT_LOGGING_RULES"] = "qt.core.qthreadstorage.warning=false;qt.qpa.*=false"

# Preserve original stdout/stderr handles before any Qt/GUI redirection
_orig_stdout = sys.__stdout__
_orig_stderr = sys.__stderr__

_orig_stdout.write("[*] Starting Clash Bot AI v2.2.7...\n")
_orig_stdout.flush()

# 2. Configure paths
root_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(root_dir)

src_dir = os.path.join(root_dir, "Source")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Add Tools/adb to system PATH
tools_adb = os.path.join(root_dir, "Tools", "adb")
if os.path.exists(tools_adb):
    os.environ["PATH"] = tools_adb + os.pathsep + os.environ.get("PATH", "")

# 3. Crash logging
crash_log = os.path.join(root_dir, "crash.log")
def log_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    err = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    _orig_stderr.write(f"\n[!] ERROR:\n{err}\n")
    _orig_stderr.flush()
    try:
        with open(crash_log, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*70}\nCRASH REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{'='*70}\n{err}")
    except Exception:
        pass

sys.excepthook = log_exception

# 4. Import modules & hook license / UI branding guards
_orig_stdout.write("[*] Loading modules...\n")
_orig_stdout.flush()

import license_manager
from ui import gui
import ui.main_window

# Disable online license kills and force update prompts
ui.main_window.MainWindow.handle_fatal_license = lambda self, *args, **kwargs: None
ui.main_window.ask_forced_update_choice = lambda *args, **kwargs: False
ui.main_window.launch_self_update = lambda *args, **kwargs: False

# Override window title formatting to enforce Clash Bot AI branding
orig_update_window_title = ui.main_window.MainWindow._update_window_title
def _branded_update_window_title(self):
    orig_update_window_title(self)
    title = self.windowTitle()
    for old_name in ["ACBot Pro", "ACBot", "AutoClash", "ClashBot"]:
        if old_name in title:
            title = title.replace(old_name, "Clash Bot AI")
    if not title.startswith("Clash Bot AI"):
        title = "Clash Bot AI v2.2.7"
    self.setWindowTitle(title)
    if hasattr(self, "titlebar_title") and self.titlebar_title:
        self.titlebar_title.setText(title)

ui.main_window.MainWindow._update_window_title = _branded_update_window_title

# Override key_status_label to reflect VIP Lifetime status for Clash Bot AI
def _branded_update_key_status(self):
    if hasattr(self, "key_status_label") and self.key_status_label:
        self.key_status_label.setMinimumWidth(160)
        self.key_status_label.setText("VIP Lifetime Active")
        self.key_status_label.setStyleSheet("background-color: rgba(56, 189, 248, 0.12); color: #7DD3FC; border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 10px; padding: 2px 12px; font-weight: 600; font-size: 11px;")

ui.main_window.MainWindow.update_key_status_label = _branded_update_key_status

def main():
    _orig_stdout.write("[*] Initializing application framework...\n")
    _orig_stdout.flush()

    from PySide6 import QtCore, QtGui, QtWidgets
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    gui.set_windows_app_user_model_id()
    gui.WINDOW_SETTINGS_APP = "Clash Bot AI"

    app = gui.QApplication.instance() or gui.QApplication(sys.argv)
    if os.name == "nt":
        style = gui.QStyleFactory.create("Fusion")
        if style:
            app.setStyle(style)

    app.setApplicationName("Clash Bot AI")
    app_icon = gui.get_app_icon()
    app.setWindowIcon(app_icon)
    app.setStyleSheet(gui.POPUP_STYLESHEET)

    gui.ensure_runtime_dirs()
    gui.cleanup_stale_onefile_tempdirs()

    # Check for update resume auto-activation marker
    auto_activate = False
    try:
        from updater_helper import consume_resume_marker
        auto_activate = bool(consume_resume_marker())
    except Exception:
        pass

    _orig_stdout.write("[+] Launching Clash Bot AI Main Window...\n")
    _orig_stdout.flush()

    window = ui.main_window.MainWindow()
    window.setWindowIcon(app_icon)
    _branded_update_window_title(window)
    _branded_update_key_status(window)

    # Attach modern Minimalist CB Monogram squircle icon to custom titlebar
    try:
        t_label = window.titlebar_title
        parent_frame = t_label.parent()
        icon_labels = [c for c in parent_frame.children() if type(c).__name__ == "QLabel" and c != t_label]
        if icon_labels:
            from PySide6.QtGui import QPixmap
            from PySide6.QtCore import Qt
            logo_file = os.path.join(root_dir, "assets", "icon.png")
            if os.path.exists(logo_file):
                pm = QPixmap(logo_file).scaled(22, 22, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon_labels[0].setPixmap(pm)
                icon_labels[0].setFixedSize(22, 22)
    except Exception as e:
        _orig_stderr.write(f"[!] Warning setting titlebar logo: {e}\n")

    # Configure razor-sharp rendering on all graphics views
    for v in window.findChildren(QtWidgets.QGraphicsView):
        v.setRenderHint(QtGui.QPainter.Antialiasing, True)
        v.setRenderHint(QtGui.QPainter.TextAntialiasing, True)
        v.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        v.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)

    # Apply Solid Glass Design System (deeplethe/solid-glass)
    try:
        # Ensure high-legibility razor-sharp typography
        for f in ["segoeui.ttf", "segoeuib.ttf", "segoeuil.ttf", "segoeuii.ttf"]:
            p = os.path.join("C:/Windows/Fonts", f)
            if os.path.exists(p):
                QtGui.QFontDatabase.addApplicationFont(p)

        crisp_font = QtGui.QFont("Segoe UI Variable Text")
        if not crisp_font.exactMatch():
            crisp_font = QtGui.QFont("Segoe UI")
        crisp_font.setPixelSize(13)
        crisp_font.setWeight(QtGui.QFont.Weight.DemiBold)
        crisp_font.setStyleStrategy(QtGui.QFont.StyleStrategy(QtGui.QFont.PreferQuality | QtGui.QFont.PreferAntialias))
        crisp_font.setHintingPreference(QtGui.QFont.PreferFullHinting)
        app.setFont(crisp_font)

        solid_glass_qss = """
        /* ===================================================================
           SOLID GLASS DESIGN SYSTEM (deeplethe/solid-glass)
           - Razor-sharp typography (Segoe UI Variable Text DemiBold)
           - Smoky acrylic glass panels with 32% specular edge lighting
           - Sleek Platinum White glass checkboxes (Zero Purple!)
           - One State clear-glass pane for active sidebar item
           - Sleek unified control dock (Start, Pause, Stop connected)
           =================================================================== */

        QMainWindow {
            background-color: #111317;
        }

        #TitleBar {
            background-color: #14171E;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            border-top: 1px solid rgba(255, 255, 255, 0.32);
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
        }

        #TitleBarTitle {
            color: #FFFFFF;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-size: 13.5px;
            font-weight: 700;
            padding-left: 4px;
        }

        #TitleMinBtn, #TitleCloseBtn {
            min-width: 34px;
            max-width: 34px;
            min-height: 26px;
            max-height: 26px;
            border-radius: 5px;
            font-size: 14px;
            color: #CBD5E1;
        }

        #TitleMinBtn:hover {
            background-color: rgba(255, 255, 255, 0.08);
            color: #FFFFFF;
        }

        #TitleCloseBtn:hover {
            background-color: #E81123;
            color: #FFFFFF;
        }

        /* Solid Glass Sidebar: Pane Standing on Edge */
        #NavPanel {
            background-color: #13161D;
            border-right: 1px solid rgba(255, 255, 255, 0.08);
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        QPushButton[nav_button="true"] {
            background-color: transparent;
            border: 1px solid transparent;
            border-left: 3px solid transparent;
            color: #E2E8F0;
            text-align: left;
            padding: 8px 12px;
            margin: 2px 8px;
            border-radius: 8px;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-size: 13px;
            font-weight: 600;
        }

        QPushButton[nav_button="true"]:hover {
            background-color: rgba(255, 255, 255, 0.07);
            color: #FFFFFF;
        }

        /* One State Active Selection: Clear Glass with 32% Top Rim Light */
        QPushButton[nav_button="true"]:checked {
            background-color: rgba(255, 255, 255, 0.09);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-top: 1px solid rgba(255, 255, 255, 0.35);
            border-left: 3px solid #F1F5F9;
            color: #FFFFFF;
            font-weight: 700;
        }

        #PageStack {
            background-color: #111317;
        }

        #BottomBar {
            background-color: #14171E;
            border-top: 1px solid rgba(255, 255, 255, 0.10);
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
        }

        /* Solid Glass Cards & GroupBoxes with 32% Specular Rim */
        QGroupBox {
            background-color: rgba(255, 255, 255, 0.028);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-top: 1px solid rgba(255, 255, 255, 0.32);
            border-radius: 10px;
            margin-top: 14px;
            padding: 16px 12px 12px 12px;
            color: #FFFFFF;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-weight: 600;
            font-size: 13px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            left: 14px;
            padding: 0 6px;
            color: #FFFFFF;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-size: 13.5px;
            font-weight: 700;
        }

        /* Crisp Checkboxes (Zero Purple, Platinum White) */
        QCheckBox {
            color: #FFFFFF;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-size: 13px;
            font-weight: 600;
            spacing: 9px;
        }

        QCheckBox::indicator {
            width: 17px;
            height: 17px;
            border-radius: 4px;
            background-color: #151821;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-top: 1px solid rgba(0, 0, 0, 0.45);
            border-bottom: 1px solid rgba(255, 255, 255, 0.16);
            image: none;
        }

        QCheckBox::indicator:hover {
            border: 1px solid rgba(255, 255, 255, 0.35);
            background-color: #1A1E29;
        }

        QCheckBox::indicator:unchecked {
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-top: 1px solid rgba(0, 0, 0, 0.45);
            border-bottom: 1px solid rgba(255, 255, 255, 0.16);
            background-color: #151821;
            image: none;
        }

        /* Checked: Sleek Platinum White Glass with Dark Checkmark */
        QCheckBox::indicator:checked {
            background-color: #F1F5F9;
            border: 1px solid rgba(255, 255, 255, 0.40);
            border-top: 1px solid #FFFFFF;
            border-bottom: 1px solid rgba(0, 0, 0, 0.40);
            image: url("assets/checkbox_check_dark.svg");
        }

        QCheckBox::indicator:checked:hover {
            background-color: #FFFFFF;
            border-top: 1px solid #FFFFFF;
        }

        /* Form Controls & Labels */
        QLabel {
            color: #F1F5F9;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-size: 13px;
            font-weight: 600;
        }

        QLineEdit, QComboBox, QSpinBox, WindowBoundComboBox {
            background-color: #161922;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-top: 1px solid rgba(0, 0, 0, 0.45);
            border-bottom: 1px solid rgba(255, 255, 255, 0.20);
            border-radius: 6px;
            padding: 5px 8px;
            color: #FFFFFF;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-size: 13px;
            font-weight: 600;
        }

        QLineEdit:focus, QComboBox:focus, QSpinBox:focus, WindowBoundComboBox:focus {
            border: 1px solid rgba(255, 255, 255, 0.35);
            border-bottom: 1px solid #F1F5F9;
            background-color: #1A1E29;
        }

        /* Tab Widgets & Navigation Panes */
        QTabWidget::pane {
            border: 1px solid rgba(255, 255, 255, 0.08);
            background-color: rgba(255, 255, 255, 0.02);
            border-radius: 8px;
        }

        QTabBar::tab {
            background-color: transparent;
            color: #CBD5E1;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', sans-serif;
            font-size: 12.5px;
            font-weight: 600;
            padding: 6px 14px;
            border-bottom: 2px solid transparent;
        }

        QTabBar::tab:hover {
            color: #FFFFFF;
            background-color: rgba(255, 255, 255, 0.05);
        }

        QTabBar::tab:selected {
            color: #FFFFFF;
            font-weight: 700;
            border-bottom: 2px solid #F1F5F9;
        }

        /* Lists and Text Viewers */
        QTextEdit, QListView, QListWidget {
            background-color: #14171E;
            color: #F8FAFC;
            font-family: 'Segoe UI Variable Text', 'Segoe UI', monospace;
            font-size: 12px;
            font-weight: 500;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
        }

        /* Sleek Unified Control Dock (Start, Pause, Stop connected into one physical glass capsule) */
        #ControlDock {
            background-color: rgba(0, 0, 0, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.10);
            border-top: 1px solid rgba(255, 255, 255, 0.32);
            border-bottom: 1px solid rgba(0, 0, 0, 0.60);
            border-radius: 9px;
        }
        #ControlDock QToolButton {
            border: none;
            background: transparent;
            padding: 2px;
        }
        #ControlDock QToolButton#MiniQuickStart {
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }
        #ControlDock QToolButton#MiniQuickStart:hover {
            background-color: rgba(52, 211, 153, 0.22);
        }
        #ControlDock QToolButton#MiniQuickStart:pressed {
            background-color: rgba(52, 211, 153, 0.35);
        }
        #ControlDock QToolButton#MiniQuickPause {
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }
        #ControlDock QToolButton#MiniQuickPause:hover {
            background-color: rgba(251, 191, 36, 0.22);
        }
        #ControlDock QToolButton#MiniQuickPause:pressed {
            background-color: rgba(251, 191, 36, 0.35);
        }
        #ControlDock QToolButton#MiniQuickStop {
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
        }
        #ControlDock QToolButton#MiniQuickStop:hover {
            background-color: rgba(239, 68, 68, 0.22);
        }
        #ControlDock QToolButton#MiniQuickStop:pressed {
            background-color: rgba(239, 68, 68, 0.35);
        }

        /* Scrollbars */
        QScrollBar:vertical {
            background: transparent;
            width: 6px;
            margin: 2px;
        }
        QScrollBar::handle:vertical {
            background: rgba(255, 255, 255, 0.16);
            border-radius: 3px;
            min-height: 20px;
        }
        QScrollBar::handle:vertical:hover {
            background: rgba(255, 255, 255, 0.30);
        }
        """

        icons_map = {
            'General': 'assets/solid_icons/General.png',
            'Attack Army': 'assets/solid_icons/Attack_Army.png',
            'Multi Village': 'assets/solid_icons/Multi_Village.png',
            'Builder Base': 'assets/solid_icons/Builder_Base.png',
            'Clan Capital': 'assets/solid_icons/Clan_Capital.png',
            'Upgrades/Research': 'assets/solid_icons/Upgrades_Research.png',
            'XP Farming': 'assets/solid_icons/XP_Farming.png',
            'Extra Modes': 'assets/solid_icons/Extra_Modes.png',
            'Bot Runtime': 'assets/solid_icons/Bot_Runtime.png',
            'Statistics': 'assets/solid_icons/Statistics.png',
            'Log': 'assets/solid_icons/Log.png',
            'Settings': 'assets/solid_icons/Settings.png',
        }

        for item in window._ui_scene.items():
            if type(item).__name__ == "QGraphicsProxyWidget":
                pw = item.widget()
                pw.setFont(crisp_font)
                
                # 1. Assign modern functional icons to navigation sidebar & clean text
                for b in pw.findChildren(QtWidgets.QPushButton):
                    txt = b.text().strip()
                    if 'Settings' in txt:
                        b.setText(' Settings')
                    for key in icons_map:
                        if key in txt and os.path.exists(icons_map[key]):
                            b.setIcon(QtGui.QIcon(icons_map[key]))
                            b.setIconSize(QtCore.QSize(18, 18))
                            break

                # 2. Apply theme stylesheet
                pw.setStyleSheet(pw.styleSheet() + solid_glass_qss)

                # 3. Refine BottomBar Action Controls & VIP Badge
                bb = pw.findChild(QtWidgets.QWidget, 'BottomBar')
                if bb:
                    lay = bb.layout()
                    start_btn = bb.findChild(QtWidgets.QToolButton, 'MiniQuickStart')
                    pause_btn = bb.findChild(QtWidgets.QToolButton, 'MiniQuickPause')
                    stop_btn = bb.findChild(QtWidgets.QToolButton, 'MiniQuickStop')
                    
                    dock = QtWidgets.QFrame(bb)
                    dock.setObjectName('ControlDock')
                    dock_lay = QtWidgets.QHBoxLayout(dock)
                    dock_lay.setContentsMargins(0, 0, 0, 0)
                    dock_lay.setSpacing(0)
                    
                    lay.removeWidget(start_btn)
                    lay.removeWidget(pause_btn)
                    lay.removeWidget(stop_btn)
                    
                    start_btn.setParent(dock)
                    pause_btn.setParent(dock)
                    stop_btn.setParent(dock)
                    
                    start_btn.setFixedSize(40, 34)
                    pause_btn.setFixedSize(38, 34)
                    stop_btn.setFixedSize(40, 34)
                    
                    start_btn.setIcon(QtGui.QIcon('assets/solid_icons/play_emerald.png'))
                    start_btn.setIconSize(QtCore.QSize(18, 18))
                    start_btn.setToolTip('Start Bot (Automated Tactical Farming)')
                    start_btn.setStyleSheet('')
                    
                    pause_btn.setIcon(QtGui.QIcon('assets/solid_icons/pause_amber.png'))
                    pause_btn.setIconSize(QtCore.QSize(18, 18))
                    pause_btn.setToolTip('Pause Bot')
                    pause_btn.setStyleSheet('')
                    
                    stop_btn.setIcon(QtGui.QIcon('assets/solid_icons/stop_ruby.png'))
                    stop_btn.setIconSize(QtCore.QSize(18, 18))
                    stop_btn.setToolTip('Stop Bot')
                    stop_btn.setStyleSheet('')
                    
                    dock_lay.addWidget(start_btn)
                    dock_lay.addWidget(pause_btn)
                    dock_lay.addWidget(stop_btn)
                    
                    lay.insertWidget(0, dock)
                    dock.show()
                    start_btn.show()
                    pause_btn.show()
                    stop_btn.show()

                    if hasattr(window, "key_status_label") and window.key_status_label:
                        window.key_status_label.setStyleSheet("background: rgba(255, 255, 255, 0.04); color: #E2E8F0; border: 1px solid rgba(255, 255, 255, 0.10); border-top: 1px solid rgba(255, 255, 255, 0.32); border-radius: 8px; padding: 4px 12px; font-weight: 600; font-size: 11px;")

                break
    except Exception as e:
        _orig_stderr.write(f"[!] Warning applying Solid Glass Theme: {e}\n")

    gui._restore_last_window_position(app, window, gui.WINDOW_MODE_MAIN)
    app.aboutToQuit.connect(lambda: gui._save_last_window_position(window, gui.WINDOW_MODE_MAIN))

    window.show()
    _orig_stdout.write("[+] Clash Bot AI is running!\n")
    _orig_stdout.flush()

    if auto_activate:
        gui.QTimer.singleShot(3000, window.start_bot)

    return app.exec()

if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        log_exception(*sys.exc_info())
        input("\nPress Enter to exit...")
        sys.exit(1)
