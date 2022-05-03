from cx_Freeze import setup, Executable

base = None

executables = [Executable("writing.py", base=base)]

packages = ["idna"]
options = {
'build_exe': {
    'build_exe': './/build'
    }
}

setup(
    name = "Writing",
    options = options,
    version = "1.0.0.0",
    description = '',
    executables = executables,
)
