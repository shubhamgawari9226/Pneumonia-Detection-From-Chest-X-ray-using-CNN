@echo off
echo Installing Python dependencies...
echo.

echo Installing core dependencies...
pip install Flask>=2.0.0
pip install numpy>=1.21.0
pip install pillow>=8.0.0

echo Installing TensorFlow...
pip install tensorflow>=2.8.0

echo Installing additional dependencies...
pip install h5py>=3.1.0
pip install gunicorn>=20.0.0

echo Installing gevent (optional)...
pip install gevent>=21.0.0

echo.
echo Installation complete!
echo You can now run: python app.py
pause