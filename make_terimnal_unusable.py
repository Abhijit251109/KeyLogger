import os
# import powershell
import termios

while True:
    DIR = os.getcwd()
    if DIR == r'Documents':
        print("Can't open folder ...")
        break

    elif DIR == r"C:\\Users":
        break
    
    else: termios.B3500000