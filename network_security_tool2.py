#!/usr/bin/env python3 

# Script Name:                         network_security_tool 
# Author name:                         Hector Cordova
# Date of latest revision:             23JAN2024 
# Purpose:                             To creat a scanning tool using scapy
# Execution:                           python3 
# Additional Resources:                https://scapy.readthedocs.io/en/latest/index.html | https://scapy.readthedocs.io/en/latest/introduction.html# | https://scapy.readthedocs.io/en/latest/extending.html | https://chat.openai.com/share/d5b54cd7-714b-4088-ac2a-8329ae747529

import sys
from scapy.all import IP, TCP, ICMP, sr, send

def get_ports_from_input(port_input):
    ports = []
    if "-" in port_input:
        start_port, end_port = map(int, port_input.split("-"))
        ports = list(range(start_port, end_port + 1))
    else:
        ports = list(map(int, port_input.split(",")))
    return ports

def scan_port(target_ip, port):
    syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
    response = sr(syn_packet, timeout=1, verbose=0)[0]

    if response is not None and response.haslayer(TCP):
        flags = response.getlayer(TCP).flags
        if flags == 0x12:  # SYN-ACK received
            rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")
        elif flags == 0x14:  # RST-ACK received
            print(f"Port {port} is closed.")
        else:
            print(f"Port {port} is filtered, and connection is silently dropped")
    else:
        print(f"Port {port} did not respond")

def icmp_ping_sweep(network_address):
    ip_addresses = [str(ip) for ip in IP(network_address).hosts()]

    online_hosts = 0

    for ip in ip_addresses:
        if IP(ip).dst != IP(network_address).network and IP(ip).dst != IP(network_address).broadcast:
            icmp_packet = IP(dst=ip) / ICMP()
            response = sr(icmp_packet, timeout=1, verbose=0)[0]

            if response is not None and response.haslayer(ICMP):
                icmp_type = response.getlayer(ICMP).type
                icmp_code = response.getlayer(ICMP).code

                if icmp_type == 0:  # Echo Reply
                    print(f"Host {ip} is online.")
                    online_hosts += 1
                elif icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                    print(f"Host {ip} actively blocking ICMP traffic.")
                else:
                    print(f"Host {ip} is unresponsive.")
            else:
                print(f"Host {ip} is unresponsive.")

    print(f"\nTotal online hosts: {online_hosts}")

def main():
    try:
        print("Network Security Tool Menu:")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            target_ip = input("Enter the target IP address: ")
            port_input = input("Enter port range (e.g., 80-100) or specific ports (e.g., 22,80,443): ")

            ports = get_ports_from_input(port_input)

            for port in ports:
                scan_port(target_ip, port)

        elif choice == 2:
            network_address = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
            icmp_ping_sweep(network_address)

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
