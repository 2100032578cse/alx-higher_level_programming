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
    url = "https://api.github.com/user"
    var1 = sys.argv[1]
    var2 = sys.argv[2]
    request = requests.get(url)
    print(request.json().get("id"))
