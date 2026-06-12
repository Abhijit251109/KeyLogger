import os

def make_file_undeletable(filepath):
    try:
        os.chmod(filepath, 0o755)
        print(f"Permissions for '{filepath}' set to .py (0o755).")
    except OSError as e:
        print(f"Error setting permissions for '{filepath}': {e}")


file_to_protect = "test_log.txt"

make_file_undeletable(file_to_protect)

try:
    os.remove(file_to_protect)
    print(f"'{file_to_protect}' was deleted.")
except OSError as e:
    print(f"Could not delete '{file_to_protect}': {e}")

