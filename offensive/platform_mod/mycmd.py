from .elevate import ElevateBase


def start_cmd():
    """Start a Windows Command Prompt session with administrator privileges when possible."""
    return ElevateBase._run_as_admin("cmd.exe", ["/k"])
