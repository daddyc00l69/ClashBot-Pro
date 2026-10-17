@echo off
title ClashBot-Pro v2.2.6 [Console Debug Mode]
cd /d "%~dp0"

echo =======================================================================
echo   ClashBot-Pro v2.2.6 - Console Debug Launcher
echo =======================================================================
echo.

set PYTHONUNBUFFERED=1

if exist "Project\venv\Scripts\python.exe" (
    "Project\venv\Scripts\python.exe" -u "run_bot.py"
) else (
    python -u "run_bot.py"
)

echo.
echo [Application Exited with code %errorlevel%]
pause
