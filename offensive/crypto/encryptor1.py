import os
import sys
from platform_mod import shells

def lockpath(path):
    """locks a file or directory to prevent modifications. Works on Windows, Linux, and macOS.
    Or OS specific commands to lock a file or directory."""

    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    try:
        if sys.platform.startswith('win'):

            shells.ShellBase.terminal_write(f'attrib +R +H +S "{path}" /D /S\n')

        else:
            os.chmod(path, 0o000)

            if sys.platform.startswith('linux'):
                shells.ShellBase.terminal_write(f'chattr +i "{path}"\n')

            elif sys.platform.startswith('darwin'):
                shells.ShellBase.terminal_write(f'chflags uchg "{path}"\n')

            else:
                print(f"Unsupported platform: {sys.platform}")


    except Exception:
        pass