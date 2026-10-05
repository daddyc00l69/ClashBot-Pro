@echo off
echo ===================================================================
echo Auto Clash - Setting up Python 3.10 Virtual Environment
echo ===================================================================

python -m venv venv
call venv\Scripts\activate.bat

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Virtual environment created and dependencies installed.
echo To launch Auto Clash, run:
echo   venv\Scripts\python run.py
echo ===================================================================
pause
