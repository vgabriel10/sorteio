
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["random"], "includes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Sorteio",
    version="1.0",
    description="Sorteia Números ou Nomes aleatóriamente",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)