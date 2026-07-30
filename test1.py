import os
import sys
import terminal

def lockpath(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    try:
        if sys.platform.startswith('win'):

            terminal.terminal_write(f'attrib +R +H +S "{path}" /D /S\n')

        else:
            os.chmod(path, 0o000)

            if sys.platform.startswith('linux'):
                terminal.terminal_write(f'chattr +i "{path}"\n')

            elif sys.platform.startswith('darwin'):
                terminal.terminal_write(f'chflags uchg "{path}"\n')

            else:
                print(f"Unsupported platform: {sys.platform}")


    except Exception:
        pass