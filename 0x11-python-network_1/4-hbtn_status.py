#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
