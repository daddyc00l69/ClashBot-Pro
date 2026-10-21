# -*- coding: utf-8 -*-
"""
Clash Bot AI v2.2.7 - Root GUI Module Proxy
Redirects root-level `import gui` calls to `ui.gui`
"""
from ui.gui import *
from ui.gui import LicenseSplash, run
import ui.gui as _ui_gui

# Expose module globals from ui.gui
for _attr in dir(_ui_gui):
    if not _attr.startswith('__') or _attr in ('__name__', '__doc__', '__file__'):
        globals()[_attr] = getattr(_ui_gui, _attr)
