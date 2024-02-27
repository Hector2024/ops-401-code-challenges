#!/usr/bin/env python3 

# Script Name:                         web_application_fingerprint.py 
# Author name:                         Hector Cordova
# Date of latest revision:             26FEB2024
# Purpose:                             a Python script that utilizes multiple banner grabbing approaches against a single target.
# Execution:                           python3 
# Additional Resources:                https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/, https://chat.openai.com/share/195abccf-2fa3-4476-ac87-66f03fcebaac



import os

def banner_grabbing_nc(target, port):
    print(f"Banner Grabbing using netcat (nc) for {target}:{port}")
    command = f"nc -v -n {target} {port}"
    os.system(command)

def banner_grabbing_telnet(target, port):
    print(f"Banner Grabbing using telnet for {target}:{port}")
    command = f"echo quit | telnet {target} {port}"
    os.system(command)

def banner_grabbing_nmap(target):
    print(f"Banner Grabbing using Nmap for {target}")
    command = f"nmap -sV {target}"
    os.system(command)

def main():
    target = input("Enter the URL or IP address: ")
    port = input("Enter the port number: ")

    banner_grabbing_nc(target, port)
    banner_grabbing_telnet(target, port)
    banner_grabbing_nmap(target)

if __name__ == "__main__":
    main()
