#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    var1 = sys.argv[1]
    len1 = len(sys.argv)
    lettr = "" if len1== 1 else var1
    payload = {"q": lettr}
    request = requests.post(url, data=payload)
    try:
        response = request.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
