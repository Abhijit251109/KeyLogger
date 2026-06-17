from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(KEY)

def load_key(TargetFile : str):

    with open(TargetFile, "rb") as file:
        original_data = file.read()

    cipher_suite = Fernet(KEY)
    encrypted_data = cipher_suite.encrypt(original_data)

    with open(TargetFile, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{TargetFile}' has been encrypted and is now protected.")

if __name__ == '__main__':
    load_key("test2.py")