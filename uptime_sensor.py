#!/usr/bin/env python3

import subprocess
import time
from datetime import datetime

def ping_host(ip):
    try:
        subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def main():
    ip_address = '192.168.1.38'

    while True:
        timestamp = datetime.now().strftime(('%Y-%m-%d %H:%M:%S.%f')[:-3])
        status = "Network Active" if ping_host(ip_address) else "Network Inactive"
        print(f"{timestamp} {status} to {ip_address}")
        time.sleep(2)

if __name__ == "__main__":
    main()



'''
Resources:
    - https://docs.python.org/3/library/subprocess.html
    - https://www.datacamp.com/tutorial/python-subprocess
    - https://github.com/raqueltianna/ops-401/blob/main/uptimesensorpt1.py
'''
