import os
import test2

def make_file_undeletable(filepath):
    try:
        os.chmod(filepath, 0o000) # Set permissions to 0o000 (no permissions)
        print(f"Permissions for '{filepath}' set to 0o000 (no permissions).")
    except OSError as e:
        print(f"Error setting permissions for '{filepath}': {e}")

if __name__ == "__main__":
    make_file_undeletable(filepath="test1.py")
    test2.load_key("logs.txt")
    test2.load_key("test1.py")
    
    
    
    
    
# Failed can't make file unreadble 