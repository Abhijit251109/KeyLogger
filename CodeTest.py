import background_runner

def codeTest():
    while True:
        try:

            with open("test.txt", "w") as testFile:
                word = "This is a test file to test codes in this directories."
                for i in word:
                    i = word*10000000
                    testFile.write(i)

        except Exception as e:
            print(f"An error {e} occurred while creating file.")
            pass

if __name__ == "__main__":
    codeTest()
