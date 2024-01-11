#!/usr/bin/env python3

import subprocess
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def ping_host(ip):
    try:
        subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def send_email(sender_email, sender_password, receiver_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def main():
    ip_address = input("Enter the IP address: ")
    sender_email = input("Enter your email address:")
    sender_password = input("Enter your email password (Gmail app): ")
    receiver_email = input("Enter the adminstrator email:")

    previous_status = None

    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        current_status = "Network Active" if ping_host(ip_address) else "Network Inactive"

        if current_status != previous_status:
            subject = "Entered IP Status Change"
            body = f"IP Status changed from {previous_status} to {current_status} at {timestamp}: {ip_address}"
            send_email(sender_email, sender_password, receiver_email, subject, body)

        print(f"{timestamp} {current_status} to {ip_address}")

        previous_status = current_status
        time.sleep(2)

if __name__ == "__main__":
    main()


'''
Resources:
https://docs.python.org/3/library/smtplib.html
https://docs.python.org/3/library/email.mime.html
https://www.w3schools.com/python/python_try_except.asp
https://github.com/Hector2024/ops-401-code-challenges/blob/main/uptime_sensor.py
https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-03/challenges/DEMO.md
https://github.com/raqueltianna/ops-401/blob/main/uptimesensorpt2.py
'''