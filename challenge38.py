#!/usr/bin/env python3

# Author:               Abdou Rockikz
# Description:          This script is designed to scan a given URL for Cross-Site Scripting (XSS) vulnerabilities
#                       by detecting and exploiting vulnerable form fields.
# Date:                 2024-02-13
# Modified by:          Hector Cordova
# Resources:            https://thepythoncode.com/article/make-a-xss-vulnerability-scanner-in-python, https://pypi.org/project/wapiti3/, https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-38/challenges/DEMO.md, https://chat.openai.com/share/195abccf-2fa3-4476-ac87-66f03fcebaac

### Before running this script, make sure to install the requests and bs4 libraries by running 'pip install requests bs4' ###

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

def get_all_forms(url):
    """
    Get all HTML forms from the provided URL.

    :param url: The URL to scrape forms from.
    :return: A list of BeautifulSoup form objects.
    """
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """
    Get details of a form.

    :param form: A BeautifulSoup form object.
    :return: A dictionary containing form details.
    """
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    """
    Submit a form with specified value.

    :param form_details: Details of the form.
    :param url: The URL to submit the form to.
    :param value: The value to submit.
    :return: Response object from the server.
    """
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    """
    Scan a URL for XSS vulnerabilities.

    :param url: The URL to scan.
    :return: True if XSS vulnerability is detected, False otherwise.
    """
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS Vulnerability')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

def main():
    """
    Main function to execute XSS vulnerability scanning on a given URL.

    Prompts the user to input a URL, scans for XSS vulnerabilities,
    and prints the results to the screen.
    """
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

if __name__ == "__main__":
    main()
