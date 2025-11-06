@echo off
echo Fixing TensorFlow compatibility issues...
echo.

echo Uninstalling current TensorFlow...
pip uninstall tensorflow -y

echo Installing compatible TensorFlow version...
pip install tensorflow==2.15.0

echo Installing Microsoft Visual C++ Redistributable dependencies...
echo Please also install Microsoft Visual C++ Redistributable if not already installed
echo Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe

echo.
echo If TensorFlow still doesn't work, try:
echo 1. Install Python 3.11 instead of 3.13
echo 2. Or use tensorflow-cpu instead of tensorflow
echo.
pause