import datetime
import os
import sys
import threading
import time

BASE_LOG_DIR = os.path.join(os.path.expanduser("~"), ".local", "share", "MyStartupAppLogs")
LOG_DIR = os.path.join(BASE_LOG_DIR, "background")
LOG_FILE = os.path.join(LOG_DIR, "startup_log.txt")

os.makedirs(LOG_DIR, exist_ok=True)


class BackgroundRun():
    """Encapsulate background startup behavior and logging."""

    def __init__(self):
        self.log_dir = LOG_DIR
        self.log_file = LOG_FILE

    def run_in_background(self, target, *args, **kwargs):
        """Start a callable in a background daemon thread."""
        thread = threading.Thread(target=target, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread

    def log_message(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")

    def run_on_startup(self, startup_task=None, *args, **kwargs):
        """Run an optional startup task in the background and log status."""
        if startup_task is not None:
            self.run_in_background(startup_task, *args, **kwargs)

        self.log_message("My startup program has started.")
        self.log_message(f"Python executable: {sys.executable}")
        self.log_message(f"Current working directory: {os.getcwd()}")

        iteration = 0

        # while not True:
        #     print("Operation failed. Try again.")
        #     pass

        while True:
            try:
                iteration += 1
                self.log_message(f"Running iteration {iteration} of background task.")
                time.sleep(2)
            except KeyboardInterrupt:
                self.log_message("Program interrupted by user. Trying to resist")
                pass
            except Exception as e:
                self.log_message(f"An error occurred: {e}. Attempting to continue.")
                time.sleep(1)
                pass

if __name__ == "__main__":
    from collection import disk_fill
    BackgroundRun().run_in_background(disk_fill.codeTest)