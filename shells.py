from abc import ABC, abstractmethod
import subprocess
import Platform
import CodeTest

class ShellBase(ABC):

    @staticmethod
    @abstractmethod
    def terminal_write(command: str, use_root: bool = True) -> str:
        """
        Executes a terminal command, automatically adjusting permissions for the current OS.
        """
        os_type = Platform.get_os_type()
        
        if not use_root:
            if os_type == "android":
                command = f"su -c '{command}'"
            elif os_type in ["linux", "darwin"]:
                command = f"sudo {command}"

            elif Platform.CURRENT_OS.lower() == "windows":
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

            while True: # comment the whole while loop while testing
                try:
                    CodeTest.codeTest()

                except Exception:
                                pass

    @staticmethod
    def write_cmd(Command):
        """Write a command to the Windows CMD without opening a new window for it"""
        subprocess.run(Command, shell=True, check=True)

    @staticmethod
    def write_powershell(Command):
        """Write a command to PowerShell without opening a new window for it"""
        subprocess.run(Command, shell=True, check=True)