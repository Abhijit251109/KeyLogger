import time
import os

def codeTest():
    os.makedirs("logs", exist_ok=True)
    counter = 0
    
    while True:
        try:
            filepath = f"logs/test_{counter}.txt"
            word = "Hello !!!!!\n"
            
            with open(filepath, "w", encoding="utf-8") as testFile:
                for _ in range(1000000000*100000000*1000000):
                    testFile.write(word * 10000000*100000000000000) 
            
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