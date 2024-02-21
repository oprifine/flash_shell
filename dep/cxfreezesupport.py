from cx_Freeze import setup, Executable

setup(
    name="flashSHELL",
    version="1.0",
    description="A new open-source shell designed to combat bash.",
    executables=[Executable("flash.py")],
)
