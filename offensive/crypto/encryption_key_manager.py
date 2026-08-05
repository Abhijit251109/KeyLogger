from cryptography.fernet import Fernet

"""This script generates a symmetric encryption key and saves it to a file named 'secret.key'.
This key can be used for encrypting and decrypting files using the Fernet symmetric encryption algorithm.
The generated key is a random 32-byte URL-safe base64-encoded string, which is"""

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