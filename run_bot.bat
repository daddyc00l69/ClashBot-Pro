@echo off
title Auto Clash - Release v2.1 (Update) Launcher
echo =========================================================
echo   Launching Auto Clash Release v2.1 (Update) from Source
echo =========================================================
cd /d "%~dp0releases\v2.1-update\Source"
python "%~dp0releases\v2.1-update\Project\run.py"
pause
