@echo off
title ClashBot-Pro v2.2.6 [VIP Unlocked]
cd /d "%~dp0"

echo =======================================================================
echo   ClashBot-Pro v2.2.6 - New Clash of Clans UI Automation Engine
echo   VIP Unlocked - No Login Key Required - Offline Mode Enabled
echo =======================================================================
echo.

:: 1. Check for Virtual Environment inside folder
if exist "venv\Scripts\python.exe" (
    set "PY_EXE=venv\Scripts\python.exe"
    goto :CHECK_DEPS
)
if exist "Project\venv\Scripts\python.exe" (
    set "PY_EXE=Project\venv\Scripts\python.exe"
    goto :CHECK_DEPS
)

:: 2. Check for system python
where python.exe >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your system PATH!
    echo.
    echo ClashBot-Pro requires Python 3.10 (64-bit).
    echo Please install Python 3.10 from:
    echo   https://www.python.org/downloads/release/python-31011/
    echo.
    echo IMPORTANT: Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

set "PY_EXE=python"

:: 3. Check Python version
for /f "tokens=2 delims= " %%v in ('%PY_EXE% --version 2^>^&1') do set "PY_VER=%%v"
echo [*] Detected Python: %PY_VER%

:: Check if version is 3.10
echo %PY_VER% | findstr /b "3.10" >nul
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] ClashBot-Pro core binaries require Python 3.10 (64-bit).
    echo Detected version %PY_VER% might cause "DLL load failed" or import errors.
    echo If the bot fails to open, install Python 3.10.11 from python.org.
    echo.
)

:CHECK_DEPS
:: 4. Check if required packages are installed
echo [*] Checking required dependencies...
%PY_EXE% -c "import PySide6, cv2, numpy, requests" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [!] Missing required Python libraries.
    echo [*] Installing dependencies automatically from requirements.txt...
    echo.
    %PY_EXE% -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Automatic installation failed!
        echo Please open command prompt here and run:
        echo   pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
    echo [+] Dependencies installed successfully!
    echo.
)

:: 5. Launch bot
echo [*] Launching ClashBot-Pro...
%PY_EXE% "run_bot.py"
set "EXIT_CODE=%errorlevel%"

if %EXIT_CODE% neq 0 (
    echo.
    echo =======================================================================
    echo [!] Bot exited with code %EXIT_CODE%.
    echo If an error occurred, check the console output above.
    echo =======================================================================
    echo.
    pause
)
