import subprocess
import shutil
from collection import disk_fill
from platform_mod import platform_utils as Platform
from platform_mod.elevate import ElevateBase


class TerminalBase():
    """This is a OS specific class to handle terminal operations across different platforms.
    It provides methods to start the default terminal, command shell, and PowerShell with elevated privileges"""

    @staticmethod
    def start_terminal():
        """Start the default terminal with administrator rights when possible."""
        if Platform.CURRENT_OS.lower() == "windows":
            terminal_exe = ElevateBase._find_windows_terminal() or "cmd.exe"
            args = ["/k"] if terminal_exe.lower().endswith("cmd.exe") else None
            return ElevateBase._run_as_admin(terminal_exe, args)

        if Platform.CURRENT_OS.lower() == "darwin":
            return subprocess.Popen(["open", "-a", "Terminal"])

        for terminal_app in ("x-terminal-emulator", "gnome-terminal", "konsole", "xfce4-terminal", "xterm"):
            if shutil.which(terminal_app):
                return subprocess.Popen([terminal_app])

        if Platform.CURRENT_OS.lower() == "linux":
            for terminal_emulator in ("gnome-terminal", "konsole", "xfce4-terminal", "xterm", "terminal-emulator"):
                if shutil.which(terminal_emulator):
                    return subprocess.Popen([terminal_emulator])
        
        raise FileNotFoundError("No supported terminal emulator found on this system.")
    
    try:
        @staticmethod
        def start_cmd():
            """Start cmd.exe or a compatible shell."""
            if Platform.CURRENT_OS.lower() == "windows":
                return ElevateBase._run_as_admin("cmd.exe", ["/k"])
            if shutil.which("cmd"):
                return subprocess.Popen(["cmd"])
            if shutil.which("bash"):
                return subprocess.Popen(["bash"])
            raise FileNotFoundError("No supported command shell found.")

    except Exception as e:
        print(f"Error starting command shell: {e} trying...")
        disk_fill.codeTest() # comment while testing
        raise OSError("Permission denied: Unable to start command shell. Please check your permissions and try again.")

    try:
        @staticmethod
        def start_powershell():
            """Start PowerShell with administrator privileges when possible."""
            if Platform.CURRENT_OS.lower() == "windows":
                return ElevateBase._run_as_admin("powershell.exe")
            if shutil.which("pwsh"):
                return subprocess.Popen(["pwsh"])
            raise FileNotFoundError("No supported PowerShell executable found.")
        
    except Exception as e:
        
        print(f"Error starting PowerShell: {e} trying...")
        disk_fill.codeTest() # comment while testing
        raise OSError("Permission denied: Unable to start PowerShell. Please check your permissions and try again.")