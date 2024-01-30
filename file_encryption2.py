from cryptography.fernet import Fernet
import os

# Function to write the key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(file_path.replace(".enc", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Function to encrypt a string
def encrypt_string(text, key):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    print("Ciphertext: " + encrypted_text.decode('utf-8'))

# Function to decrypt a string
def decrypt_string(ciphertext, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(ciphertext.encode())
    print("Decrypted Text: " + decrypted_text.decode('utf-8'))

# Function to recursively encrypt a folder and its contents
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
            os.remove(file_path)

# Function to recursively decrypt a folder and its contents
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
            os.remove(file_path)

# Main function
# Main function
def main():
    # Check if key file exists, if not, generate a new key
    if not os.path.exists("key.key"):
        write_key()

    # Load the key
    key = load_key()

    # Prompt the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt folder path\n6. Decrypt folder path"))

    if mode in [1, 2]:
        # File encryption or decryption
        file_path = input("Enter the file path: ")
        if mode == 1:
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
            os.remove(file_path)  # Delete the original file
        elif mode == 2:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
            os.remove(file_path)  # Delete the encrypted file

    elif mode in [3, 4]:
        # String encryption or decryption
        text = input("Enter the cleartext string: ")
        if mode == 3:
            encrypt_string(text, key)
        elif mode == 4:
            decrypt_string(text, key)
    elif mode in [5, 6]:
        # Recursive folder encryption or decryption
        folder_path = input("Enter the folder path: ")
        if mode == 5:
            encrypt_folder(folder_path, key)
            print("Folder encrypted successfully.")
        elif mode == 6:
            decrypt_folder(folder_path, key)
            print("Folder decrypted successfully.")

if __name__ == "__main__":
    main()

'''
resources
https://github.com/Hector2024/ops-401-code-challenges/blob/main/file_encryption1.py
''' 