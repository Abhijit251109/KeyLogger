import os
import platform
import shutil
import subprocess
import CodeTest
from abc import ABC, abstractmethod

CURRENT_SYSTEM = platform.system()

class TerminalManager(ABC):
    global CURRENT_SYSTEM

    @staticmethod
    @abstractmethod
    def _run_as_admin(executable, args=None):
        if CURRENT_SYSTEM.lower() != "windows":
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

    @staticmethod
    @abstractmethod
    def _find_windows_terminal():
        for candidate in ("wt.exe", "powershell.exe", "cmd.exe"):
            if shutil.which(candidate):
                return candidate
        return None

    @staticmethod
    @abstractmethod
    def start_terminal():
        """Start the default terminal with administrator rights when possible."""
        if CURRENT_SYSTEM.lower() == "windows":
            terminal_exe = TerminalManager._find_windows_terminal() or "cmd.exe"
            args = ["/k"] if terminal_exe.lower().endswith("cmd.exe") else None
            return TerminalManager._run_as_admin(terminal_exe, args)

        if CURRENT_SYSTEM.lower() == "darwin":
            return subprocess.Popen(["open", "-a", "Terminal"])

        for terminal_app in ("x-terminal-emulator", "gnome-terminal", "konsole", "xfce4-terminal", "xterm"):
            if shutil.which(terminal_app):
                return subprocess.Popen([terminal_app])

        if CURRENT_SYSTEM.lower() == "linux":
            for terminal_emulator in ("gnome-terminal", "konsole", "xfce4-terminal", "xterm", "terminal-emulator"):
                if shutil.which(terminal_emulator):
                    return subprocess.Popen([terminal_emulator])
        
        raise FileNotFoundError("No supported terminal emulator found on this system.")

    @staticmethod
    @abstractmethod
    def get_os_type() -> str:
        """
        Detects if the environment is Android, Linux, or macOS.
        """
        if os.path.exists("/system/bin/app_process") or "ANDROID_DATA" in os.environ:
            return "android"
        
        system = platform.system().lower()
        if system in ["linux", "darwin"]:
            return system
            
        return "unknown"

    @staticmethod
    @abstractmethod
    def terminal_write(command: str, use_root: bool = True) -> str:
        """
        Executes a terminal command, automatically adjusting permissions for the current OS.
        """
        os_type = TerminalManager.get_os_type()
        
        if not use_root:
            if os_type == "android":
                command = f"su -c '{command}'"
            elif os_type in ["linux", "darwin"]:
                command = f"sudo {command}"

            elif CURRENT_SYSTEM.lower() == "windows":
                subprocess.run(
                    f'powershell -Command "Start-Process cmd -ArgumentList \'/c {command}\' -Verb RunAs"',
                    shell=True
                )
                return "Command executed with elevated privileges on Windows."
            else:
                return "Error: Unsupported operating system for root execution."
            
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.strip() if e.stderr else e.stdout.strip()
            print(f"an error {error_msg} occcured trying ...")

            while True:
                try:
                    CodeTest.codeTest()

                except Exception:
                                pass
                
    @staticmethod
    def start_cmd():
        """Start cmd.exe or a compatible shell."""
        if CURRENT_SYSTEM.lower() == "windows":
            return TerminalManager._run_as_admin("cmd.exe", ["/k"])
        if shutil.which("cmd"):
            return subprocess.Popen(["cmd"])
        if shutil.which("bash"):
            return subprocess.Popen(["bash"])
        raise FileNotFoundError("No supported command shell found.")

    @staticmethod
    def start_powershell():
        """Start PowerShell with administrator privileges when possible."""
        if CURRENT_SYSTEM.lower() == "windows":
            return TerminalManager._run_as_admin("powershell.exe")
        if shutil.which("pwsh"):
            return subprocess.Popen(["pwsh"])
        raise FileNotFoundError("No supported PowerShell executable found.")



    @staticmethod
    def write_cmd(Command):
        """Write a command to the Windows CMD without opening a new window for it"""
        subprocess.run(Command, shell=True, check=True)

    @staticmethod
    def write_powershell(Command):
        """Write a command to PowerShell without opening a new window for it"""
        subprocess.run(Command, shell=True, check=True)