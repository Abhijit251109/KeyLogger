KeyLogger

«⚠️ Educational Cybersecurity / Malware-Research Project

This repository is a personal cybersecurity learning project designed to study Python, operating-system behavior, platform abstraction, privilege handling, persistence concepts, input collection, encryption, and destructive-malware techniques in controlled environments.

Do not run this project on systems or data that you do not own or have explicit authorization to test.»

---

Overview

KeyLogger is a modular Python project that started as an experiment with keyboard input monitoring and gradually evolved into a broader cybersecurity research project.

The current version is organized primarily under an "offensive/" package and contains several independent components for experimenting with:

- Cross-platform operating-system detection
- Command-line interfaces
- Terminal and shell abstraction
- Privilege elevation
- Background execution
- Keyboard input collection
- Persistence-related behavior
- File and directory manipulation
- Encryption experiments
- Disk-filling behavior
- System-destruction concepts
- Android/Linux/macOS/Windows platform differences

The repository is work in progress and is being refactored toward a cleaner, more maintainable Python architecture.

---

⚠️ Safety Notice

Some modules in this repository intentionally contain destructive or malware-like functionality.

Examples include:

- Keyboard input logging
- Attempts to execute commands with elevated privileges
- Writing files into privileged system locations
- Taking ownership of protected Windows files
- Disk-filling routines
- File/directory permission manipulation
- Encryption and file-locking experiments
- Code that demonstrates deletion of critical operating-system directories

These components are included for cybersecurity education and controlled experimentation.

Recommended environment

If experimenting with the project:

- Use a disposable virtual machine.
- Take a VM snapshot before testing.
- Do not use a production computer.
- Do not use real credentials or sensitive information.
- Disconnect the test environment from unnecessary networks.
- Keep important files outside the test environment.
- Test destructive functionality only against disposable files and directories.

---

Current Architecture

The repository is currently divided into functional packages:

KeyLogger-master/
│
├── README.md
├── .gitignore
│
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       └── codeql.yml
│
└── offensive/
    │
    ├── __init__.py
    ├── main.py
    │
    ├── collection/
    │   ├── __init__.py
    │   ├── disk_fill.py
    │   ├── keylogger.py
    │   └── os_destroyer.py
    │
    ├── core/
    │   ├── __init__.py
    │   ├── background_runner.py
    │   ├── base.py
    │   └── manager.py
    │
    ├── crypto/
    │   ├── __init__.py
    │   ├── encryption_key_manager.py
    │   └── encryptor1.py
    │
    ├── persistence/
    │   ├── __init__.py
    │   ├── keyboard_interrupt_suppress.py
    │   ├── os_root_save.py
    │   └── ownership_steal.py
    │
    └── platform_mod/
        ├── __init__.py
        ├── android_shell_util.py
        ├── elevate.py
        ├── mycmd.py
        ├── platform_utils.py
        ├── powershell.py
        └── shells.py

---

Package Description

"offensive/"

Contains the main experimental components of the project.

The package is intentionally separated from the repository root so that the project can eventually be expanded with additional components such as defensive or analysis tooling.

---

"offensive/collection/"

Contains modules related to data collection and destructive experiments.

"keylogger.py"

Implements keyboard-event monitoring using "pynput".

The current implementation writes captured keyboard events to:

logs.txt

It also contains a "start_keylogger()" entry point for starting the listener.

---

"disk_fill.py"

Contains the project's disk-filling experiment.

The module repeatedly generates large text files inside a local:

logs/

directory.

It also maintains a separate activity log under the user's local application-data area.

«Warning: This routine can rapidly consume disk space and should only be executed in a disposable test environment.»

---

"os_destroyer.py"

Contains experimental code demonstrating operating-system destruction techniques.

Separate routines exist for:

- Windows
- Linux
- macOS
- Android

The module demonstrates how malware could theoretically target critical operating-system directories.

«This module should not be executed on a real or important system.»

---

"offensive/core/"

Contains common execution and coordination logic.

"base.py"

Contains base abstractions used by other components.

The goal of this module is to provide reusable interfaces for functionality that may have different implementations depending on the operating system.

---

"manager.py"

Contains higher-level management functionality, including terminal-related coordination.

The CLI can use the manager to start terminal functionality.

---

"background_runner.py"

Provides functionality for running tasks in background daemon threads.

It also records information such as:

- Startup events
- Python executable
- Working directory
- Background-task iterations
- Exceptions
- Interrupt attempts

The module is currently experimental and contains intentionally persistent execution behavior.

---

"offensive/platform_mod/"

Contains platform-specific functionality and shell abstractions.

"platform_utils.py"

Provides operating-system detection.

The project currently recognizes:

Windows
Linux
macOS
Android

The module also avoids relying on a locally shadowed "platform.py" by explicitly importing the standard-library "platform" module.

---

"elevate.py"

Contains abstractions for privilege elevation.

Depending on the platform, it can experiment with mechanisms such as:

- Windows UAC elevation
- "sudo" on Unix-like systems

---

"shells.py"

Provides an abstract shell interface for executing commands.

It contains experimental handling for:

- Windows
- Linux
- macOS
- Android

It also contains command helpers for Windows CMD and PowerShell.

---

"mycmd.py"

Provides a small Windows CMD launcher built on the elevation abstraction.

---

"powershell.py"

Provides a PowerShell launcher through the project's terminal abstractions.

---

"android_shell_util.py"

Contains Android-oriented shell execution functionality.

It can experiment with commands executed through Android's "su" mechanism when available.

---

"offensive/persistence/"

Contains experiments related to persistence, privilege handling, and privileged filesystem operations.

"keyboard_interrupt_suppress.py"

Contains an experimental loop intended to continue running despite "KeyboardInterrupt".

It interacts with the keyboard-collection component.

---

"os_root_save.py"

Provides cross-platform functions for writing data to privileged/root locations.

The implementation contains separate handling for:

- Windows
- Linux
- macOS
- Android

It also contains Windows UAC and Unix "sudo" experimentation.

«This functionality should only be tested inside an isolated environment.»

---

"ownership_steal.py"

Contains Windows-specific experiments involving:

- Administrative privilege detection
- "takeown"
- "icacls"
- Protected-file ownership
- File deletion

This demonstrates techniques that malware could use to manipulate protected files.

---

"offensive/crypto/"

Contains encryption-related experiments.

"encryption_key_manager.py"

Uses the "cryptography" package and Fernet symmetric encryption.

The current implementation generates a key and uses it for file encryption experiments.

---

"encryptor1.py"

Contains filesystem-locking experiments.

Depending on the platform, it can experiment with:

- Windows file attributes
- Linux permissions / immutable attributes
- macOS file flags

The purpose is to study how operating systems restrict modification of files.

---

Command-Line Interface

The primary entry point is:

offensive/main.py

The CLI is based on Python's "argparse" module.

It supports several modes.

Operating-System Information

python main.py --os-info

This displays the detected operating system.

---

Terminal

python main.py --start-terminal

Starts the project's terminal-management functionality.

---

Windows CMD

python main.py --start-cmd

Attempts to start CMD using the project's elevation abstraction.

---

PowerShell

python main.py --start-powershell

Attempts to start PowerShell using the project's platform abstraction.

---

Module Execution

Individual modules can be requested using:

python main.py --module MODULE

A specific function can also be supplied:

python main.py --module MODULE --function FUNCTION

For example:

python main.py --module collection.keylogger --function start_keylogger

«Only run modules whose behavior you understand and whose execution is safe for your test environment.»

---

Dry Run

The CLI also provides a dry-run mode:

python main.py --module collection.keylogger --dry-run

or:

python main.py --run-all --dry-run

Dry-run mode reports what would be selected without executing the requested module actions.

---

Run All

The CLI contains a predefined collection of project modules that can be selected using:

python main.py --run-all

Because the repository contains destructive and persistent components, running all modules is not recommended on a normal operating system.

For development, prefer selecting one harmless component at a time.

---

Dependencies

The project currently relies on Python's standard library as well as external packages.

Important external dependencies include:

pynput
cryptography

Install them with:

pip install pynput cryptography

A virtual environment is strongly recommended:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Activate it on Linux/macOS:

source .venv/bin/activate

Then install the required packages.

---

Python Version

The project is written for modern Python 3.

A recommended development environment is:

Python 3.10+

Individual modules may have additional operating-system-specific requirements.

---

Development

The project is currently undergoing a structural refactor.

The main development priorities are:

- Cleaner package boundaries
- Better naming
- Reduced duplicated code
- Better exception handling
- More consistent type hints
- Improved logging
- Better abstractions
- Cross-platform reliability
- Automated testing
- Better CLI behavior
- Documentation

---

Testing

Automated tests are planned as the project architecture stabilizes.

The intended testing strategy is based around:

pytest

Tests should primarily verify:

- Platform detection
- CLI argument handling
- Module discovery
- Function resolution
- Error handling
- Shell abstraction behavior
- Non-destructive filesystem operations
- Encryption utilities
- Background-runner behavior

Destructive functionality should not be tested directly against a host operating system.

---

Code Quality

The project uses GitHub automation and CodeQL configuration through:

.github/

The long-term goal is to combine:

- "pytest"
- Static analysis
- CodeQL
- Formatting/linting
- Type checking
- CI testing

into a consistent development workflow.

---

Design Principles

The project is being developed around several software-engineering principles:

Modularity

Each major responsibility should have its own module or package.

Separation of concerns

Platform-specific code should remain separate from general application logic.

Reusability

Common functionality should be implemented once and reused through abstractions.

Explicit interfaces

Base classes and abstractions should define common behavior between platform implementations.

Maintainability

The code should gradually become easier to understand, test, and modify.

Controlled experimentation

Potentially destructive cybersecurity experiments should remain isolated from normal development code and tested only in authorized environments.

---

Project Status

🚧 Work in Progress

The repository is currently functional in several areas but is not considered production-ready.

Some components are experimental, some APIs are inconsistent, and several modules still require refactoring.

The project should currently be viewed as a cybersecurity research and software-engineering learning project, rather than a finished framework.

---

Roadmap

Phase 1 — Architecture

- [x] Introduce "offensive/" package
- [x] Separate collection functionality
- [x] Separate core functionality
- [x] Separate platform functionality
- [x] Separate persistence functionality
- [x] Separate crypto functionality
- [ ] Standardize module naming
- [ ] Improve package interfaces

Phase 2 — Reliability

- [ ] Improve cross-platform behavior
- [ ] Remove fragile imports
- [ ] Improve exception handling
- [ ] Improve CLI error messages
- [ ] Add structured logging
- [ ] Add configuration management

Phase 3 — Testing

- [ ] Add pytest test suite
- [ ] Add CLI tests
- [ ] Add platform-detection tests
- [ ] Add mock-based shell tests
- [ ] Add filesystem-operation tests
- [ ] Add CI test workflow

Phase 4 — Documentation

- [ ] Document public APIs
- [ ] Add architecture diagrams
- [ ] Document supported platforms
- [ ] Document testing procedures
- [ ] Add developer documentation

Phase 5 — Defensive Research

A future direction of the project is to add defensive and analysis-oriented tooling so that the repository can also demonstrate how the behaviors implemented here can be detected and mitigated.

---

Responsible Use

This project should only be used:

- On systems you own
- In an authorized cybersecurity laboratory
- Inside disposable virtual machines
- For educational research
- For malware-analysis experiments
- For defensive security research

Do not deploy the project against third-party systems, collect other people's input, destroy data, bypass security controls, or obtain unauthorized privileges.

---

License

No license has currently been specified for this repository.

Until a license is added, the source code should not be assumed to be freely redistributable or reusable.

---

Author's Note

This project is primarily a learning exercise.

The goal is not simply to create functional code, but to understand how different pieces of Python software interact with an operating system and how malware-like behaviors can be structured into independent components.

As the project evolves, the focus is shifting toward:

Better architecture
        ↓
Better testing
        ↓
Better documentation
        ↓
Better understanding
        ↓
Better defensive security knowledge

Use responsibly. Learn safely. Test in isolation.
