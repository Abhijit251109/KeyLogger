import os
import importlib

_std_platform = importlib.import_module("platform")
CURRENT_OS : str = _std_platform.system().lower()

"""
A base class for platform-specific functionality.
"""

@staticmethod
def get_os_type() -> str:
    """
    Detects if the environment is Android, Linux, or macOS.
    """
    if os.path.exists("/system/bin/app_process") or "ANDROID_DATA" in os.environ:
        return "android"
        
    system = CURRENT_OS.lower()
    if system in ["linux", "darwin"]:
        return system

    elif system == "windows":
        return "windows"
            
    else:
        return "unknown"