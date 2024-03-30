#!/bin/bash
#Bash script that takes in a URL and displays all
curl -s -X PUT  -d "user_id=98" -H "Origin: You got me!" -L 0.0.0.0:5000/catch_me
