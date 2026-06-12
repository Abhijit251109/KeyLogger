import datetime
import test
import time
import os
import sys

LOG_DIR = os.path.join(os.path.expanduser("~"), ".local", "share", "MyStartupAppLogs")
LOG_FILE = os.path.join(LOG_DIR, "startup_log.txt")

os.makedirs(LOG_DIR, exist_ok=True)

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def run_on_startup():
    log_message("My startup program has started.")
    log_message(f"Python executable: {sys.executable}")
    log_message(f"Current Working Directory: {os.getcwd()}")

    iteration = 0
    while True:
        try:
            iteration += 1
            log_message(f"Running iteration {iteration} of background task.")
            time.sleep(10)
        except KeyboardInterrupt:
            log_message("Program interrupted by Ctrl+C. Exiting.")
            break
        except Exception as e:
            log_message(f"An error occurred: {e}. Attempting to continue.")
            time.sleep(5)

# test.run_forever()

if __name__ == "__main__":
    test.run_forever("background_runner.py")