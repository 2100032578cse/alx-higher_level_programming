#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    var1 = sys.argv[1]
    var2 = sys.argv[2]
    auth = HTTPBasicAuth(var1, var2)
    request = requests.get(url, auth=auth)
    print(request.json().get("id"))
