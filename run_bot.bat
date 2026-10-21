@echo off
title Clash Bot AI v2.2.7 [VIP Unlocked]
cd /d "%~dp0"

echo =======================================================================
echo   Clash Bot AI v2.2.7 - Clash of Clans Automation Engine
echo   VIP Unlocked - Offline Lifetime Mode Enabled
echo =======================================================================
echo.

set "PY_CMD="

:: 1. Check direct Python 3.10 installation in LocalAppData
if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    set "PY_CMD=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    goto :FoundPython
)

:: 2. Check py launcher
where py >nul 2>&1
if %errorlevel% equ 0 (
    set "PY_CMD=py -3.10"
    goto :FoundPython
)

:: 3. Check system PATH python
where python >nul 2>&1
if %errorlevel% equ 0 (
    set "PY_CMD=python"
    goto :FoundPython
)

echo [ERROR] Python 3.10 is not installed or not found in system PATH!
echo Please ensure Python 3.10 is installed.
echo.
pause
exit /b 1

:FoundPython
echo [*] Python engine located.
echo [*] Launching Clash Bot AI v2.2.7...
echo.

"%PY_CMD%" run_bot.py
set "EXIT_CODE=%errorlevel%"

echo.
echo =======================================================================
echo [*] Clash Bot AI process completed (Exit code: %EXIT_CODE%).
echo =======================================================================
echo.
pause

