#!/usr/bin/python3

# Script Name:                          port_scanner.py 
# Author name:                          Hector Cordova
# Date of latest revision:              06MAR2024
# Purpose:                              to determine if a target port is open or closed,
# Execution:                            python3 
# Additional Resources:                 https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-44/challenges/DEMO.md, https://docs.python.org/3/library/socket.html, https://chat.openai.com/share/195abccf-2fa3-4476-ac87-66f03fcebaac



import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5  # Set a timeout value here. You can adjust it as needed.
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ")  # Collect a host IP from the user.
portno = int(input("Enter the port number: "))  # Collect a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0:  # Replace "FUNCTION" with the appropriate socket.function call
        print("Port open")
    else:
        print("Port closed")

portScanner(portno)
