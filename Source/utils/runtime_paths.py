# -*- coding: utf-8 -*-
"""
ClashBot-Pro - Runtime Path Resolver
Target Path: utils/runtime_paths.py
Architecture: x86-64 / AMD64 | Platform: Windows
Runtime: CPython 3.10+
Provenance: Native Path Architecture for ClashBot-Pro
"""

import os
import sys
from pathlib import Path

# Determine directories
_CURRENT_DIR = Path(__file__).resolve().parent       # Source/utils
_SOURCE_DIR = _CURRENT_DIR.parent                   # Source
_PROJECT_ROOT = _SOURCE_DIR.parent                  # Root directory

def is_frozen() -> bool:
    """Check if running in a frozen executable context (Nuitka/PyInstaller)."""
    return getattr(sys, "frozen", False)

def bundle_root() -> Path:
    """Returns the bundle/source directory."""
    if is_frozen():
        return Path(sys.executable).parent
    return _SOURCE_DIR

def app_root() -> Path:
    """Returns the application/source directory."""
    if is_frozen():
        return Path(sys.executable).parent
    return _SOURCE_DIR

def resolve_resource_path(relative_path) -> Path:
    """
    Intelligently resolves a resource path by checking dedicated asset directories
    (Resources/, Dependencies/, Config/, Source/) without requiring duplicate files or junctions.
    Returns a Path object.
    """
    clean_rel = str(relative_path).lstrip("/\\").replace("\\", "/")
    root = _PROJECT_ROOT

    # 1. Check inside Resources/ (for templates, assets, locales)
    for prefix in ("templates", "assets", "locales"):
        if clean_rel == prefix or clean_rel.startswith(prefix + "/"):
            target = root / "Resources" / clean_rel
            if target.exists():
                return target

    # 2. Check inside Dependencies/ (for Tools)
    if clean_rel == "Tools" or clean_rel.startswith("Tools/"):
        target = root / "Dependencies" / clean_rel
        if target.exists():
            return target

    # 3. Check inside Config/ (for treasureloot, profiles, bot.config)
    for prefix in ("treasureloot", "profiles", "bot.config"):
        if clean_rel == prefix or clean_rel.startswith(prefix + "/"):
            target = root / "Config" / clean_rel
            if target.exists():
                return target

    # 4. Check Source directory
    source_target = _SOURCE_DIR / clean_rel
    if source_target.exists():
        return source_target

    # 5. Check root directory directly
    direct_target = root / clean_rel
    if direct_target.exists():
        return direct_target

    # Fallbacks
    for prefix in ("templates", "assets", "locales"):
        if clean_rel.startswith(prefix):
            return root / "Resources" / clean_rel

    if clean_rel.startswith("Tools"):
        return root / "Dependencies" / clean_rel

    return _SOURCE_DIR / clean_rel

def resolve_writable_path(relative_path) -> Path:
    """Resolves a writable path for logs, profiles, configs."""
    clean_rel = str(relative_path).lstrip("/\\").replace("\\", "/")
    
    # Direct profiles or configs to Config/
    if clean_rel.startswith("profiles") or clean_rel == "bot.config":
        return _PROJECT_ROOT / "Config" / clean_rel
        
    return _SOURCE_DIR / clean_rel

def ensure_runtime_dirs():
    """Ensures required runtime output directories exist."""
    for d in ("logs",):
        target = _SOURCE_DIR / d
        target.mkdir(parents=True, exist_ok=True)
    for d in ("Config/profiles",):
        target = _PROJECT_ROOT / d
        target.mkdir(parents=True, exist_ok=True)

def cleanup_stale_onefile_tempdirs():
    """No-op for clean source distribution."""
    pass
