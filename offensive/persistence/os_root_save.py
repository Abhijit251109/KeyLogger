import os
import platform
import subprocess
import sys
import tempfile


def get_os_type() -> str:
    """Detects the underlying OS environment."""
    if os.path.exists("/system/bin/app_process") or "ANDROID_DATA" in os.environ:
        return "android"
    system = platform.system().lower()
    return system if system in ["linux", "darwin", "windows"] else "unknown"


def is_windows_admin() -> bool:
    """Checks for Windows administrative privileges."""
    try:
        import ctypes

        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def elevate_windows_script():
    """Triggers the Windows UAC elevation prompt."""
    import ctypes

    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )


def write_to_root(
    filename: str, file_content: str, desktop_password: str = None
) -> str:
    """Writes a text file to the system root across Windows, Linux, macOS, and Android."""
    os_type = get_os_type()

    # 1. Define Root Paths based on OS
    if os_type == "windows":
        target_path = os.path.join("C:\\", filename)
    elif os_type in ["linux", "darwin"]:
        target_path = f"/root/{filename}"
    elif os_type == "android":
        target_path = f"/{filename}"
    else:
        return "Error: Unsupported operating system."

    # 2. Windows Path: Native write if admin token is active
    if os_type == "windows":
        if not is_windows_admin():
            print("Requesting Windows Administrator Privileges...")
            elevate_windows_script()
            return "UAC prompt initiated. Check your taskbar."
        try:
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(file_content)
            return f"Successfully saved to Windows root: {target_path}"
        except Exception as e:
            return f"Windows Write Failed: {str(e)}"

    # 3. Unix Platforms (Linux, macOS, Android): Use secure staging + shell copy
    # Python cannot natively inject passwords into file operations, so we write to a
    # temp file first, then use elevated shell binaries to move it into root.
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, encoding="utf-8"
        ) as temp_file:
            temp_file.write(file_content)
            temp_path = temp_file.name

        # Construct specific elevation strategies
        if os_type == "android":
            # Uses Android's internal toolbox 'mv' command
            final_command = f"su -c 'mv \"{temp_path}\" \"{target_path}\" && chmod 644 \"{target_path}\"'"
            input_data = None
        else:
            if not desktop_password:
                os.unlink(temp_path)
                return "Error: Sudo password required for Linux/macOS root execution."
            # Uses desktop 'mv' with '-S' to accept password from stdin securely
            final_command = f"sudo -S mv '{temp_path}' '{target_path}' && sudo -S chmod 644 '{target_path}'"
            input_data = f"{desktop_password}\n"

        # Execute system move operation
        result = subprocess.run(
            final_command,
            shell=True,
            capture_output=True,
            text=True,
            input=input_data,
            check=True,
        )

        # Cleanup if something remained
        if os.path.exists(temp_path):
            os.unlink(temp_path)

        return f"Successfully saved to root: {target_path}"

    except subprocess.CalledProcessError as e:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        error_output = e.stderr.strip() if e.stderr else e.stdout.strip()
        if "read-only file system" in error_output.lower():
            return f"Blocked: {target_path} is heavily locked down (Read-Only File System) by the kernel."
        return f"Privileged Execution Failed: {error_output}"