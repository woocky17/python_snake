@echo off
REM Activar el entorno virtual y ejecutar snake.py sin consola
call ".venv\Scripts\activate.bat"
start "" pythonw snake.py
