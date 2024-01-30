#!/usr/bin/env python3 

# Script Name:                         automated_brute_force_tool 
# Author name:                         Hector Cordova
# Date of latest revision:             29JAN2024 
# Purpose:                             To create a automated brute force tool
# Execution:                           python3 
# Additional Resources:                https://www.geeksforgeeks.org/iterate-over-a-set-in-python/, https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz, https://github.com/raqueltianna/ops-401/blob/main/opschallenge16.py, https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-16/challenges/DEMO.md

import time

# Prompt user to select mode 
def offensive_mode():

# ask user for path of the word file 
    word_list_path = input("Enter the path to the word list file: ")
# ask user for how long of a delay 
    delay = float(input("Enter the delay between words: "))
    
# open the  word file and iterate through each line
    with open(word_list_path, 'r') as file:
        for line in file:
            word = line.strip()
            time.sleep(delay)
# print current word 
            print(f"Current: {word}")

def defensive_mode():
# ask user to put in password or string 
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
    
    mode = input("Enter 1 for offensive mode or 2 for defensive mode: ")

    if mode == '1':
        offensive_mode()
    elif mode == '2':
        defensive_mode()
    else:
        print("Please enter 1 or 2.")