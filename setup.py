from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base)
]

setup(name='PyItor',
      version = '0.2',
      description = 'A text editor written in PyQt5',
      options = dict(build_exe = buildOptions),
      executables = executables)
