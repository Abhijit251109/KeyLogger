# keeps the code running forever

import sys
import time

def _suppress_keyboard_interrupt(exctype, value, tb):
    if exctype is KeyboardInterrupt:
        return
    sys.__excepthook__(exctype, value, tb)

sys.excepthook = _suppress_keyboard_interrupt


def run_forever(str):

    str = "background_runner.py"
    while True:
        try:
            print("hellooooooooooooooo", flush=True)
            time.sleep(3)
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
    run_forever()
