@echo off
title ClashBot-Pro v2.2.6 [VIP Unlocked]
cd /d "%~dp0"

echo =======================================================================
echo   ClashBot-Pro v2.2.6 - New Clash of Clans UI Automation Engine
echo   VIP Unlocked - No Login Key Required - Offline Mode Enabled
echo =======================================================================
echo.

if exist "Project\venv\Scripts\python.exe" (
    "Project\venv\Scripts\python.exe" "run_bot.py"
    goto :eof
)

if exist "venv\Scripts\python.exe" (
    "venv\Scripts\python.exe" "run_bot.py"
    goto :eof
)

python "run_bot.py"
if %errorlevel% neq 0 (
    py -3.10 "run_bot.py"
)
