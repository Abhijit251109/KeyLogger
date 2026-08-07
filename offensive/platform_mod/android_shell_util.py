import shutil
import subprocess

def terminal_write(command: str, usr_root=True):
    if not usr_root:
        if shutil.which("su"):
            command = f"su -c '{command}'"
        else:
            command = f"sudo {command}"

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        print(f"an error {e} occurred trying to run")
        return ""
