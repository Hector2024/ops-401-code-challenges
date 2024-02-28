#!/usr/bin/env python3 

# Script Name:                      opschallenge37.py
# Author Name:                      Hector Cordova
# Date of Latest Revision:          27FEB24
# Purpose:                          
# Execution                         python3 opschallenge37.py 
# Additional Resources:             https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-37/challenges/DEMO.md, https://github.com/raqueltianna/ops-401/blob/main/code%20/opschallenge37.py


import requests
import webbrowser

# Target site URL
targetsite = "http://www.whatarecookies.com/cookietest.asp"

# Send request to get the cookie
response = requests.get(targetsite)
cookie = response.cookies

# Function to send the cookie back to the site, receive HTTP response, and generate HTML file
def send_cookie_and_capture_response(cookie):
    # Send request back to the site with the cookie
    response = requests.get(targetsite, cookies=cookie)
    
    # Generate HTML file to capture response content
    with open("response.html", "w") as html_file:
        html_file.write(response.text)
    
    # Open the HTML file with Firefox
    firefox_path = "/usr/bin/firefox"  # Modify this path according to your system
    webbrowser.get(firefox_path).open_new_tab("response.html")

# Function to bring forth the cookie monster
def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

# Call functions
bringforthcookiemonster()
print("Target site is " + targetsite)
print("Cookie:", cookie)
