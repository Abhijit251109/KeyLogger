import os
import sys
import ctypes
import subprocess
import time

def is_admin():
    """This file contains a function to check if the current user has administrative privileges on Windows.
    It uses the `ctypes` library to call the Windows API function `IsUserAnAdmin`, which returns a non-zero value if the user is an administrator and zero otherwise.
    The function returns `True` if the user is an administrator and `False` otherwise. If an exception occurs while checking for administrative privileges, the function returns `False`.
    This function is designed to work only on Windows operating systems.
    This takes ownership from the TrustedInstaller and grants full access permissions to the Administrators group for a specified file or directory, allowing it to be deleted or modified.
    It uses the `takeown` and `icacls` commands to change ownership and permissions, respectively. The function first checks if the current user has administrative privileges using the `is_admin` function.
    If the user is an administrator, it attempts to take ownership and grant full access permissions to the specified file or directory.
    If successful, it deletes the file or directory. If any errors occur during this process, such as permission issues or unexpected exceptions, they are caught and printed to the console.
    If the user is not an administrator, the function attempts to relaunch itself with elevated privileges using `ShellExecuteW`. This function is designed to work only on Windows operating systems."""

    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def rem_root_dir(file_path:str):

    if is_admin():
        if not os.path.exists(file_path):
            print("Error: The targeted file path does not exist.")
            sys.exit()

        exe_name = os.path.basename(file_path)
        print(f"Targeting protected system file: {exe_name}")

        subprocess.run(["taskkill", "/F", "/IM", exe_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.5)

        try:
            print("Taking file ownership away from TrustedInstaller...")
            subprocess.run(["takeown", "/A", "/F", file_path], check=True, stdout=subprocess.DEVNULL)

            print("Granting Full Access permissions to Administrators...")
            subprocess.run(["icacls", file_path, "/grant", "Administrators:F"], check=True, stdout=subprocess.DEVNULL)

            os.remove(file_path)
            print(f"🔥 Success! System-locked file '{exe_name}' has been completely removed.")

        except subprocess.CalledProcessError as e:
            print(f"Security override failed. The OS blocked the permission shift: {e}")
        except PermissionError:
            print("Error: Ownership was changed, but the file is still hard-locked by a running service or kernel process.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        input("\nPress Enter to close...")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)