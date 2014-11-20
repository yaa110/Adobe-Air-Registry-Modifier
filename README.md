# Adobe Air Registry Modifier

This project intended to provide an integration between Adobe Air projects and Windows Registry by which it is possible to modify Windows Registry in Adobe Air projects. As Adobe Air is a cross-platform SDK, thus there is no Class to modify Windows Registry. However, it could be done using `NativeProcess` class and an interface tool between Adobe Air and Windows Registry such as Python.

## Installation

1. Install [Python 2.7.x](https://www.python.org/downloads/)
2. Download [py2exe](http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download) and install it.
3. In order to make `process.exe` file, open Command Prompt:
  * `cd src-python`.
  * `c:\PATH_TO_PYTHON\python.exe setup.py py2exe`.
4. Then, `process.exe` would be found in `dist` folder.

**Note:** In Adobe Air manifest file, use `<supportedProfiles>extendedDesktop desktop</supportedProfiles>` to be allowed to use `NativeProcess`.

## How to use

1. Instantiate `RegistryModify` class: `RegistryModify rm = new RegistryModify("RELATIVE_PATH_TO_PROCESS.EXE");`
2. Root Keys (as `_rootkey` parameter): `HKEY_LOCAL_MACHINE`, `HKEY_CLASSES_ROOT`, `HKEY_CURRENT_CONFIG`, `HKEY_CURRENT_USER` and `HKEY_USERS`
3. Example of `_path` parameter: `Software\Microsoft\Office\11.0\Common\General`
4. Example of `_key` parameter: `RecentFiles`
