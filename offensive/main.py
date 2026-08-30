"""Command-line entry point for the project."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path


ROOT = Path(__file__).resolve().parent

LOG_FILE = ROOT / "project.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    filename=LOG_FILE,
)

logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    """Build and return the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Project command-line entry point"
    )

    parser.add_argument(
        "--os-info",
        action="store_true",
        help="Request OS information.",
    )

    parser.add_argument(
        "--start-terminal",
        action="store_true",
        help="Request terminal startup.",
    )

    parser.add_argument(
        "--start-cmd",
        action="store_true",
        help="Request command-shell startup.",
    )

    parser.add_argument(
        "--start-powershell",
        action="store_true",
        help="Request PowerShell startup.",
    )

    parser.add_argument(
        "--module",
        action="append",
        metavar="MODULE",
        help="Specify a module to run.",
    )

    parser.add_argument(
        "--function",
        help="Function associated with a module.",
    )

    parser.add_argument(
        "--run-all",
        action="store_true",
        help="Request execution of all configured modules.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Display planned actions without executing them.",
    )

    return parser


def get_planned_actions(args: argparse.Namespace) -> list[str]:
    """Return the actions requested by the command line."""
    actions: list[str] = []

    if args.os_info:
        actions.append("get OS information")

    if args.start_terminal:
        actions.append("start terminal")

    if args.start_cmd:
        actions.append("start command shell")

    if args.start_powershell:
        actions.append("start PowerShell")

    if args.run_all:
        actions.append("run all configured modules")

    for module in args.module or []:
        if args.function:
            actions.append(f"run {module}:{args.function}")
        else:
            actions.append(f"run {module}")

    return actions


def handle_dry_run(args: argparse.Namespace) -> int:
    """Report requested actions without importing or executing them."""
    actions = get_planned_actions(args)

    if not actions:
        actions.append("no project action")

    for action in actions:
        message = "Dry run: would %s"
        logger.info(message, action)
        print(message % action)

    return 0


def main() -> int:
    """Application entry point."""
    parser = build_parser()
    args = parser.parse_args()

    logger.info("Application started; dry_run=%s", args.dry_run)

    # ---------------------------------------------------------------
    # IMPORTANT:
    # This MUST happen before any project-module imports or execution.
    # ---------------------------------------------------------------
    if args.dry_run:
        return handle_dry_run(args)

    # Keep operational module dispatch out of this safe skeleton.
    #
    # Non-operational application functionality can be called here.
    logger.info("No safe non-operational action was requested.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
