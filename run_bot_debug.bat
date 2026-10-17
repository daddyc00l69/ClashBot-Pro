@echo off
title ClashBot-Pro v2.2.6 [Console Debug Mode]
cd /d "%~dp0"

echo =======================================================================
echo   ClashBot-Pro v2.2.6 - Console Debug Mode
echo =======================================================================
echo.

set PYTHONUNBUFFERED=1

if exist "venv\Scripts\python.exe" (
    set "PY_EXE=venv\Scripts\python.exe"
) else if exist "Project\venv\Scripts\python.exe" (
    set "PY_EXE=Project\venv\Scripts\python.exe"
) else (
    set "PY_EXE=python"
)

where %PY_EXE% >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found in PATH or venv!
    echo Please install Python 3.10 from https://www.python.org/downloads/release/python-31011/
    echo.
    pause
    exit /b 1
)

echo [*] Using Python executable:
%PY_EXE% -c "import sys; print('   Python Version:', sys.version); print('   Executable:', sys.executable)"
echo.

echo [*] Starting ClashBot-Pro with full console output...
%PY_EXE% -u "run_bot.py"
set "EXIT_CODE=%errorlevel%"

echo.
echo =======================================================================
echo [Process Terminated] Application exited with code %EXIT_CODE%
echo =======================================================================
echo.
pause
