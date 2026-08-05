import os
import subprocess
import ctypes
from abc import ABC, abstractmethod
from offensive.platform import platform_utils as Platform
import shutil

class ElevateBase(ABC):
    """This is a OS specific class to handle elevation of privileges for executing commands in the terminal.
      It provides methods to run commands as an administrator on Windows or as root on Linux and macOS."""

    @staticmethod
    @abstractmethod
    def _run_as_admin(executable, args=None):
        if Platform.CURRENT_OS.lower() != "windows":
            command = [executable] + (args or [])
            return subprocess.Popen(command)

        params = None
        if args:
            params = " ".join(args) if isinstance(args, (list, tuple)) else str(args)

        os.system("")

        ShellExecuteW = ctypes.windll.shell32.ShellExecuteW
        ret = ShellExecuteW(None, "runas", executable, params, None, 1)
        if int(ret) <= 32:
            raise OSError(f"Failed to elevate {executable}: error code {ret}")
        return ret

    def _find_windows_terminal():
        possible_terminals = ["wt.exe", "WindowsTerminal.exe", "cmd.exe", "powershell.exe"]
        for terminal in possible_terminals:
            if shutil.which(terminal):
                return terminal
        return None

    def _run_as_root(executable, args=None):

        if Platform.CURRENT_OS.lower() in ["linux", "darwin"]:
            command = [executable] + (args or [])
            return subprocess.Popen(["sudo"] + command)