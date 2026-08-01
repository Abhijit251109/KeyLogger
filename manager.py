import Platform
# import CodeTest
import base
import shells
import elevate

class TerminalManager:
    """
    A manager class to handle terminal operations across different platforms.
    """

    OS = Platform.get_os_type()

    if OS.lower() == "windows":
        base_class = base.TerminalBase
        shell_class = shells.ShellBase
        elevation = elevate.ElevateBase

        try:
            elevation._run_as_admin("cmd.exe", ["/k"])  # Attempt to elevate privileges
            base_class.start_terminal() or base_class.start_cmd() or base_class.start_powershell()

        except Exception as e:

            print(f"Error starting terminal: {e} trying...")
            # CodeTest.codeTest()  # comment while testing
            raise OSError("Permission denied: Unable to start terminal. Please check your permissions and try again.")

    elif OS.lower() in ["linux", "darwin"]:
        base_class = base.TerminalBase
        shell_class = shells.ShellBase
        elevation = elevate.ElevateBase

        try:
            elevation._run_as_root("bash")  # Attempt to elevate privileges
            base_class.start_terminal()

        except Exception as e:

            print(f"Error starting terminal: {e} trying...")
            # CodeTest.codeTest()  # comment while testing
            raise OSError("Permission denied: Unable to start terminal. Please check your permissions and try again.")

    else:
        print(f"Unsupported operating system: {OS}. Terminal operations may not work as expected.")

if __name__ == "__main__":
    TerminalManager()