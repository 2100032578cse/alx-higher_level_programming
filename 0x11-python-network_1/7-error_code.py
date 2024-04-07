#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8).
"""
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
