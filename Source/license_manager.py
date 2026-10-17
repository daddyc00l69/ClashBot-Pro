# -*- coding: utf-8 -*-
"""
ClashBot-Pro - License Manager (VIP Unlocked Engine)
Module Name: license_manager
Target Path: license_manager.py
Architecture: x86-64 / AMD64 | Platform: Windows
Runtime: CPython 3.10.11

Autonomous license bypass module:
- Completely removes login key requirement
- Provides offline local authentication with Lifetime Unlimited validity
- Decrypts and supplies the AES fixed points coordinate data key
- Bypasses remote telemetry and network heartbeat checks
"""

import os
import sys
import base64
import hashlib
import json
import platform
import secrets
import subprocess
import threading
import time
import uuid

# Base paths and environment definitions
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
LICENSE_FILE = os.path.join(BASE_PATH, '..', 'Config', 'license.key')
CURRENT_VERSION = '2.2.6'
SERVER_URL = 'https://api.acbot.site/validate'
TRANSIENT_FAILURE_GRACE_SECONDS = 900
_ANDROID_ID_ENV_VAR = 'AUTOCLASH_ANDROID_ID'
_DATA_KEY_ENV_VAR = 'AUTOCLASH_DATA_KEY'
_RETRY_INTERVAL_SECONDS = 180
_HWID_V3_PLACEHOLDER_VALUES = {'', 'none', 'unknown', 'to be filled by o.e.m.', 'default string'}

# Embedded AES data key for offline fixed_points decryption
_AES_KEY_B64 = 'biFuGXVXDQplk6oBL1lx5yC1udHMNnmQnvh3ISSgreM='
_data_key_cache = base64.b64decode(_AES_KEY_B64)
_heartbeat_stop_event = threading.Event()
_hwid_v3_components_cache = {
    'guid': 'unlocked-guid-0000-000000000000',
    'cpu': 'unlocked-cpu-x86_64',
    'bios': 'unlocked-bios-system'
}
license_meta_cache = {}

# Compatibility classes and exceptions
class InvalidSignature(Exception):
    """Raised on invalid signature (compatibility stub)."""
    pass

Ed25519PublicKey = None
_SERVER_PUBLIC_KEY = None


def version_tuple(v):
    """Parse version string into tuple of integers."""
    return tuple(int(x) for x in str(v).replace('v', '').split('.') if x.isdigit())


def resolve_writable_path(name):
    """Resolve writable configuration file path."""
    config_dir = os.path.join(BASE_PATH, '..', 'Config')
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, name)


def _clean_hw_marker(v):
    return str(v or '').strip()


def _collect_v3_markers():
    return dict(_hwid_v3_components_cache)


def _get_windows_machine_guid():
    return 'unlocked-guid-0000-000000000000'


def _hash_hwid_markers(*args, **kwargs):
    return 'unlocked-hwid-hash'


def _android_device_id():
    return os.environ.get(_ANDROID_ID_ENV_VAR, 'unlocked-android-device')


def _build_validation_payload(key=None):
    return {'key': key or 'VIP_UNLOCKED', 'version': CURRENT_VERSION}


def _cache_data_key(k):
    global _data_key_cache
    if isinstance(k, str):
        _data_key_cache = base64.b64decode(k)
    else:
        _data_key_cache = k


def get_cached_data_key():
    """Return decoded AES key for decrypting assets & fixed_points."""
    return _data_key_cache


def _canonical_signed_bytes(*args, **kwargs):
    return b''


def _verify_signed_response(*args, **kwargs):
    return True


def _is_transient_validation_failure(res):
    return False


def _is_valid_response(res):
    if isinstance(res, dict):
        return bool(res.get('valid', True))
    return True


def _remove_legacy_session_file():
    pass


def format_remaining(seconds):
    """Format remaining license duration for UI display."""
    return 'Lifetime Unlimited'


def get_hwid_legacy():
    return 'unlocked-legacy-hwid'


def get_hwid_v2():
    return 'unlocked-v2-hwid'


def get_hwid_v3_components():
    return dict(_hwid_v3_components_cache)


def get_license_error_message(res=None):
    """Return empty error string since license is always valid."""
    return ''


def load_key():
    """Load license key - returns empty as no key is required."""
    return ''


def load_saved_key():
    """Load saved license key - returns empty as no key is required."""
    return ''


def save_key(key):
    """No-op: do not write any login key."""
    pass


def clear_key():
    """Clear key."""
    pass


def clear_saved_key():
    """Clear saved key."""
    pass


def load_license_meta():
    """Return active license metadata dict."""
    return {
        'valid': True,
        'status': 'valid',
        'role': 'admin',
        'expires': '2099-12-31',
        'remaining': 'Lifetime Unlimited',
        'version': CURRENT_VERSION
    }


def save_license_meta(meta):
    """No-op metadata storage."""
    pass


def _validate_once(*args, **kwargs):
    return validate_license_details()


def _post_validate(*args, **kwargs):
    return validate_license_details()


def validate_license_details(key=None, *args, **kwargs):
    """
    Offline validation engine:
    Instantly returns a valid VIP Lifetime license with AES data key.
    No network connection or login key required.
    """
    return {
        'valid': True,
        'status': 'valid',
        'reason': None,
        'expires': '2099-12-31',
        'expires_at': '2099-12-31',
        'remaining': 'Lifetime Unlimited',
        'seconds_left': 999999999,
        'hwid': 'unlocked-hwid',
        'hwid_v2': 'unlocked-hwid',
        'hwid_legacy': 'unlocked-hwid',
        'raw': {
            'data_key': _AES_KEY_B64,
            'download_url': '',
            'expires': '2099-12-31',
            'force_update': False,
            'hwid': 'unlocked-hwid',
            'issued_at': '2026-10-17T00:00:00.000000Z',
            'latest_version': CURRENT_VERSION,
            'matched_hwid': 'v3',
            'nonce': 'unlocked-nonce',
            'role': 'admin',
            'seconds_left': 999999999,
            'signature': '',
            'status': 'valid',
            'update_download_url': ''
        },
        'latest_version': CURRENT_VERSION,
        'download_url': '',
        'update_download_url': '',
        'force_update': False,
        'update_available': False
    }


def start_license_heartbeat(*args, **kwargs):
    """Heartbeat stub: keeps license alive without network polling."""
    _heartbeat_stop_event.clear()


def stop_license_heartbeat(*args, **kwargs):
    """Stop heartbeat stub."""
    _heartbeat_stop_event.set()
