#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        htmlbody = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(htmlbody)))
        print("\t- content: {}".format(htmlbody))
        print("\t- utf8 content: {}".format(htmlbody.decode('utf8')))
