import os
import platform

CURRENT_OS : str = platform.system().lower()

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