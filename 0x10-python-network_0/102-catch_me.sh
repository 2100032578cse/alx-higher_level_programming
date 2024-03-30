#!/bin/bash
#Bash script that takes in a URL and displays all
curl -s -X PUT -H "Orgin: You got me!" -d "user_id=98" -L 0.0.0.0:5000/catch_me
