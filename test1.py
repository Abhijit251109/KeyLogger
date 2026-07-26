import os
import test2
import sys
import subprocess
import stat
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

# def make_file_undeletable(filepath):
#     try:
#         os.chmod(filepath, 0o000) # Set permissions to 0o000 (no permissions)
#         print(f"Permissions for '{filepath}' set to 0o000 (no permissions).")
#     except OSError as e:
#         print(f"Error setting permissions for '{filepath}': {e}")

# if __name__ == "__main__":
#     test2.load_key("logs.txt")
#     test2.load_key("test1.py")
#     make_file_undeletable(filepath="test1.py")
    
    
    
    
    
# Failed can't make file unreadble 