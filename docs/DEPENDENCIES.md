# Comprehensive Dependencies & Runtime Audit: ClashBot-Pro

## 1. Executive Summary

This document provides a complete inventory and separation analysis of all third-party libraries, framework dependencies, native shared libraries, compiled Python extensions (`.pyd`), and external utility tools embedded within the **ClashBot-Pro** (`ClashBot-Pro Application Engine`) distribution.

The application relies on an embedded **CPython 3.10.11 64-bit** execution environment bundled with **PySide6 (Qt 6.x)**, **OpenCV**, **Tesseract OCR**, and **Android Debug Bridge (ADB)** tooling.

---

## 2. Python Framework & Third-Party Library Inventory

| Library | Version | License | Category | Functional Purpose in ClashBot-Pro |
|---|---|---|---|---|
| **PySide6** | 6.11.2 | LGPLv3 / Commercial | GUI Framework | Primary graphical interface, dark styling, dashboard widgets |
| **PySide6_Essentials** | 6.11.2 | LGPLv3 | GUI Core | Core Qt6 widgets, signals, slots, layout managers |
| **PySide6_Addons** | 6.11.2 | LGPLv3 | GUI Addons | SVG rendering, concurrent threading, network access |
| **shiboken6** | 6.11.2 | LGPLv3 | Binding Layer | CPython-to-C++ object bridge for PySide6 |
| **opencv-python** | 5.0.0.93 | Apache-2.0 | Vision Engine | Fast multi-scale visual template matching (`cv2.matchTemplate`) |
| **numpy** | 2.2.6 | BSD-3-Clause | Numerical Math | Pixel buffer manipulation, coordinate array transformations |
| **pillow (PIL)** | 12.3.0 | HPND | Imaging | Screenshot cropping, PIL Image to OpenCV NumPy conversions |
| **pytesseract** | 0.3.13 | Apache-2.0 | OCR Interface | Python wrapper invoking Tesseract OCR for text recognition |
| **adbutils** | 2.12.0 | MIT | Android Bridge | Low-overhead socket client communicating with emulator ADB daemon |
| **uiautomator2** | 3.7.0 | MIT | UI Automation | Android Accessibility-based UI interaction and touch injection |
| **psutil** | 7.2.2 | BSD-3-Clause | System Monitor | Tracking BlueStacks/LDPlayer processes, memory, and CPU limits |
| **requests** | 2.34.2 | Apache-2.0 | Networking | HTTP client for remote license verification and update checks |
| **urllib3** | 2.7.0 | MIT | Networking | HTTP connection pooling, retry handling, and SSL verification |
| **cryptography** | 50.0.1 | Apache-2.0 / BSD | Security | AES decryption of `fixed_points_data.enc`, license hashing |
| **cffi** | 2.1.1 | MIT | FFI | C Foreign Function Interface for cryptography |
| **lxml** | 6.1.3 | BSD | XML Processing | Parsing UIAutomator2 XML hierarchy dumps |
| **click** | 8.5.0 | BSD-3-Clause | CLI Toolkit | Command-line option parsing for background helper tools |
| **retry2** | 0.9.5 | Apache-2.0 | Resilience | Connection retry decorators for ADB socket dropouts |
| **certifi** | 2026.7.22 | MPL-2.0 | SSL Certificates| Mozilla CA bundle for HTTPS requests validation |
| **charset-normalizer** | 3.5.1 | MIT | Encodings | Character encoding detection for network payloads |
| **idna** | 3.19 | BSD-like | Networking | Internationalized Domain Names in Applications handling |
| **tomli** | 2.4.1 | MIT | Config Parsing | TOML configuration parser |

---

## 3. Native C/C++ Runtime & Shared Libraries (.dll)

The payload bundles 50 native Dynamic Link Libraries (`.dll`):

### 3.1 Core Runtimes
- `python310.dll` (CPython 3.10.11 AMD64 runtime engine)
- `python3.dll` (CPython ABI forwarder)
- `msvcp140.dll`, `msvcp140_1.dll`, `msvcp140_2.dll` (Microsoft Visual C++ 2015–2022 Runtime)
- `mfc140u.dll` (Microsoft Foundation Classes runtime)

### 3.2 Qt 6.x Shared Libraries
- `pyside6.abi3.dll` (PySide6 C++ binding engine)
- `shiboken6.abi3.dll` (Shiboken C++ binding generator runtime)
- `qt6core.dll` (Qt6 Core library: event loop, strings, timers)
- `qt6gui.dll` (Qt6 GUI engine: rendering, fonts, windows)
- `qt6widgets.dll` (Qt6 UI widgets: buttons, tables, tab widgets, sliders)
- `qt6network.dll` (Qt6 Network stack)
- `qt6svg.dll` (Qt6 SVG vector rendering)
- `qt6concurrent.dll` (Qt6 multi-threaded processing)
- `qt6pdf.dll`, `qt63dcore.dll`

### 3.3 Numerical & Linear Algebra
- `libscipy_openblas64_-13e2df515630b4a41f92893938845698.dll` (20.39 MB OpenBLAS optimized matrix accelerator for NumPy)
- `libcrypto-1_1.dll`, `libssl-1_1.dll` (OpenSSL 1.1.1 cryptographic engine)
- `libffi-7.dll` (Foreign function interface library)

---

## 4. Compiled Python Extension Modules (.pyd)

The payload contains 97 compiled CPython extensions (`.pyd`):

### 4.1 Heavy Extensions
- `cv2\cv2.pyd` (74.82 MB - Complete OpenCV 5.x computer vision library with AVX2 optimizations)
- `pyarmor_runtime_015394\pyarmor_runtime.pyd` (PyArmor native bytecode execution interceptor)
- `numpy
andom\_sfc64.pyd`, `numpy
andom\_pcg64.pyd`, `numpy\linalg\_umath_linalg.pyd`

### 4.2 Windows Win32 API Extensions
- `win32api.pyd`, `win32gui.pyd`, `win32file.pyd`, `win32event.pyd` (Low-level Win32 window management and process hooks)
- `win32clipboard.pyd`, `win32process.pyd`, `win32con.pyd`

### 4.3 Python Standard Library Extensions
- `_asyncio.pyd`, `_bz2.pyd`, `_ctypes.pyd`, `_decimal.pyd`, `_hashlib.pyd`, `_lzma.pyd`, `_multiprocessing.pyd`, `_socket.pyd`, `_ssl.pyd`, `_zoneinfo.pyd`, `select.pyd`, `unicodedata.pyd`

---

## 5. External Bundled Tools & Auxiliary Binaries

Located in `Recovered_Source\Dependencies\Tools\`:

### 5.1 Android Debug Bridge (ADB)
- Path: `Tools\adb\`
- Files: `adb.exe`, `AdbWinApi.dll`, `AdbWinUsbApi.dll`
- Purpose: Direct connection to BlueStacks/LDPlayer emulators over TCP sockets (`127.0.0.1:5556` / `127.0.0.1:5555`).

### 5.2 Tesseract OCR Engine
- Path: `Tools\tesseract\`
- Files: `tesseract.exe`, `tessdata\osd.traineddata` (10.56 MB Orientation and Script Detection model), config profiles
- Auxiliary JARs: `ScrollView.jar`, `jaxb-api-2.3.1.jar`, `piccolo2d-core-3.0.1.jar`, `piccolo2d-extras-3.0.1.jar`
- Purpose: In-game OCR reading of loot numbers, troop counts, shield timers, and Town Hall level numbers.

### 5.3 UIAutomator2 Daemon Assets
- Path: `Tools\uiautomator2_data\`
- Files: Android APK binaries and agent assets deployed to the emulator for accessibility touch injection.

---

## 6. Separation of Application Code vs. Third-Party Code

To preserve architectural clarity, the recovered repository strictly isolates proprietary/application logic from third-party frameworks:

```
[Application Code] -> Recovered_Source/Source/
  - Contains 75 application modules (attack logic, farming loops, UI dashboard, config systems)
  - Contains bundled pyarmor_runtime_015394 for seamless dual-mode execution

[Third-Party Code] -> Recovered_Source/Dependencies/
  - Wheels manifest: requirements.txt, wheels_manifest.json
  - External binaries: Tools/adb, Tools/tesseract, Tools/uiautomator2_data
  - Native DLLs inventory: native_dlls_manifest.json
```
