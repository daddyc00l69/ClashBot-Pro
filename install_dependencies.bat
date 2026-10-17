@echo off
title ClashBot-Pro - Dependencies Installer
cd /d "%~dp0"

echo =======================================================================
echo   ClashBot-Pro v2.2.6 - One-Click Dependencies Installer
echo =======================================================================
echo.

where python.exe >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your system PATH!
    echo.
    echo ClashBot-Pro requires Python 3.10 (64-bit).
    echo Please download and install Python 3.10 from:
    echo   https://www.python.org/downloads/release/python-31011/
    echo.
    echo IMPORTANT: Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo [*] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [*] Installing all required dependencies from requirements.txt...
python -m pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo =======================================================================
    echo [+] SUCCESS! All dependencies are installed and ready.
    echo You can now double-click "run_bot.bat" to start ClashBot-Pro!
    echo =======================================================================
) else (
    echo.
    echo [ERROR] Installation failed. Please check the error messages above.
)

echo.
pause
