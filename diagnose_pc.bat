@echo off
title ClashBot-Pro System Diagnostics
cd /d "%~dp0"

set "REPORT=DIAGNOSTIC_REPORT.txt"
echo ======================================================================= > "%REPORT%"
echo   ClashBot-Pro System & Environment Diagnostic Report >> "%REPORT%"
echo   Generated on: %DATE% %TIME% >> "%REPORT%"
echo ======================================================================= >> "%REPORT%"
echo. >> "%REPORT%"

echo =======================================================================
echo   ClashBot-Pro Diagnostic Tool
echo   Testing environment on this PC...
echo =======================================================================
echo.

echo [1/6] Operating System Info:
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type" >> "%REPORT%" 2>&1
type "%REPORT%"

echo.
echo [2/6] Checking Python in PATH...
echo --- Python in PATH --- >> "%REPORT%"
where python >> "%REPORT%" 2>&1
python --version >> "%REPORT%" 2>&1
if %errorlevel% neq 0 (
    echo [FAIL] Python is NOT found or NOT in PATH!
    echo [FAIL] Python is NOT found or NOT in PATH! >> "%REPORT%"
) else (
    echo [OK] Python is installed.
)

echo.
echo [3/6] Checking Virtual Environments...
echo --- Virtual Environments --- >> "%REPORT%"
if exist "venv\Scripts\python.exe" (
    echo Found local venv >> "%REPORT%"
    venv\Scripts\python.exe --version >> "%REPORT%" 2>&1
) else (
    echo No local venv found >> "%REPORT%"
)

echo.
echo [4/6] Testing Python modules and imports...
echo --- Python Module Import Tests --- >> "%REPORT%"
python -c "
import sys
print('Python Executable:', sys.executable)
print('Python Version:', sys.version)

modules = [
    'PySide6', 'PySide6.QtWidgets', 'PySide6.QtCore', 'PySide6.QtGui',
    'cv2', 'numpy', 'PIL', 'requests', 'psutil',
    'adbutils', 'pytesseract', 'cryptography', 'zstandard'
]

for m in modules:
    try:
        __import__(m)
        print(f'[OK] {m}')
    except Exception as e:
        print(f'[FAIL] {m}: {e}')
" >> "%REPORT%" 2>&1

echo.
echo [5/6] Testing ClashBot-Pro core imports & PyArmor runtime...
echo --- ClashBot-Pro Core Imports --- >> "%REPORT%"
python -c "
import sys, os
sys.path.insert(0, r'Source')
try:
    import pyarmor_runtime_015394
    print('[OK] pyarmor_runtime_015394 loaded')
except Exception as e:
    print(f'[FAIL] pyarmor_runtime_015394: {e}')

try:
    import license_manager
    print('[OK] license_manager loaded')
except Exception as e:
    print(f'[FAIL] license_manager: {e}')

try:
    import gui
    print('[OK] gui module loaded')
except Exception as e:
    print(f'[FAIL] gui module: {e}')

try:
    import ui.main_window
    print('[OK] ui.main_window loaded')
except Exception as e:
    print(f'[FAIL] ui.main_window: {e}')
" >> "%REPORT%" 2>&1

echo.
echo [6/6] Checking recent crash log...
echo --- Recent crash.log --- >> "%REPORT%"
if exist "crash.log" (
    type "crash.log" >> "%REPORT%"
) else (
    echo No crash.log found >> "%REPORT%"
)

echo.
echo =======================================================================
echo   Diagnostic Finished!
echo   Report saved to: %~dp0%REPORT%
echo =======================================================================
echo.
echo Opening report now...
start notepad "%REPORT%"
pause
