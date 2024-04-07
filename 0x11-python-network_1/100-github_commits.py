#!/usr/bin/python3
"""  Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    var1 = sys.argv[1]
    var2 = sys.argv[2]
    url = "https://api.github.com/repos/{var2}/{var1}/commits"
    request = requests.get(url)
    commts = request.json()
    try:
        for item in range(10):
            print("{}: {}".format(
                commts[item].get("sha"),
                commts[item].get("commit").get("author").get("name")))
    except IndexError:
        pass
