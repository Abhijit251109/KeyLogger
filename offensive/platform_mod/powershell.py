def start_powershell():
    """Start PowerShell with administrator privileges when possible."""
    from core.base import TerminalBase
    return TerminalBase.start_powershell()
