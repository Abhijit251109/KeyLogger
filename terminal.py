import os
import platform
import shutil
import subprocess
import sys

CURRENT_SYSTEM = platform.system()


def _run_as_admin(executable, args=None):
    if CURRENT_SYSTEM != "Windows":
        command = [executable] + (args or [])
        return subprocess.Popen(command)

    params = None
    if args:
        params = " ".join(args) if isinstance(args, (list, tuple)) else str(args)

    os.system("")
    import ctypes

    ShellExecuteW = ctypes.windll.shell32.ShellExecuteW
    ret = ShellExecuteW(None, "runas", executable, params, None, 1)
    if int(ret) <= 32:
        raise OSError(f"Failed to elevate {executable}: error code {ret}")
    return ret


def _find_windows_terminal():
    for candidate in ("wt.exe", "powershell.exe", "cmd.exe"):
        if shutil.which(candidate):
            return candidate
    return None


def start_terminal():
    """Start the default terminal with administrator rights when possible."""
    if CURRENT_SYSTEM == "Windows":
        terminal_exe = _find_windows_terminal() or "cmd.exe"
        args = ["/k"] if terminal_exe.lower().endswith("cmd.exe") else None
        return _run_as_admin(terminal_exe, args)

    if CURRENT_SYSTEM == "Darwin":
        return subprocess.Popen(["open", "-a", "Terminal"])

    for terminal_app in ("x-terminal-emulator", "gnome-terminal", "konsole", "xfce4-terminal", "xterm"):
        if shutil.which(terminal_app):
            return subprocess.Popen([terminal_app])

    raise FileNotFoundError("No supported terminal emulator found on this system.")


def start_cmd():
    """Start cmd.exe or a compatible shell."""
    if CURRENT_SYSTEM == "Windows":
        return _run_as_admin("cmd.exe", ["/k"])
    if shutil.which("cmd"):
        return subprocess.Popen(["cmd"])
    if shutil.which("bash"):
        return subprocess.Popen(["bash"])
    raise FileNotFoundError("No supported command shell found.")


def start_powershell():
    """Start PowerShell with administrator privileges when possible."""
    if CURRENT_SYSTEM == "Windows":
        return _run_as_admin("powershell.exe")
    if shutil.which("pwsh"):
        return subprocess.Popen(["pwsh"])
    raise FileNotFoundError("No supported PowerShell executable found.")
