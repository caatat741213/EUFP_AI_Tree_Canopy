@echo off
setlocal
cd /d "%~dp0"
echo.
echo ==============================================================
echo  CanopyIQ Streamlit Demo
echo ==============================================================
echo Installing / checking demo dependencies...
python -m pip install -r requirements-demo.txt
if errorlevel 1 (
  echo.
  echo Dependency installation failed. Confirm Python is available in this terminal.
  pause
  exit /b 1
)
echo.
echo Starting CanopyIQ...
python -m streamlit run app.py
endlocal
