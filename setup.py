from cx_Freeze import setup,Executable
setup(
    name="EmpowerPy",
    version=0.1,
    description="OpencV BasedProject",
    executables=[Executable("Loginpage.py",base="Win32GUI")],
)