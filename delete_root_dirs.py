import os
import sys
import ctypes
import subprocess
import time

def is_admin():
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