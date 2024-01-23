#!/usr/bin/env python3 

# Script Name:                         network_security_tool 
# Author name:                         Hector Cordova
# Date of latest revision:             22JAN2024 
# Purpose:                             To creat a scanning tool using scapy
# Execution:                           python3 
# Additional Resources:                https://scapy.readthedocs.io/en/latest/index.html | https://scapy.readthedocs.io/en/latest/introduction.html# | https://scapy.readthedocs.io/en/latest/extending.html | https://chat.openai.com/share/e6f85381-e226-44a5-9c05-8cc43cbf8bee

import sys
from scapy.all import IP, TCP, sr1, send

# Take user input for the target IP address
target_ip = input("Enter the target IP address: ")

# Take user input for the port range or specific ports
port_input = input("Enter port range (e.g., 80-100) or specific ports (e.g., 22,80,443): ")

# Parse the port input and create a list of ports
ports = []
if "-" in port_input:
    start_port, end_port = map(int, port_input.split("-"))
    ports = list(range(start_port, end_port + 1))
else:
    ports = list(map(int, port_input.split(",")))

# Use a for loop to test each port
for port in ports:
    # Create a SYN packet
    syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

    # Send the SYN packet and receive the response
    response = sr1(syn_packet, timeout=1, verbose=0)

    # Analyze the response and take appropriate actions
    if response and response.haslayer(TCP):
        flags = response.getlayer(TCP).flags
        if flags == 0x12:  # SYN-ACK received
            # Send RST packet to graciously close the connection
            rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")
        elif flags == 0x14:  # RST-ACK received
            print(f"Port {port} is closed.")
        else:
            print(f"Port {port} is filtered and connection is silently dropped")
    else:
        print(f"Port {port} did not respond")