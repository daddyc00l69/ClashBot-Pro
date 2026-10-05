@echo off
echo Setting up Python virtual environment for ClashBot-Pro...
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo Environment ready.
pause
