#!/bin/bash
#Bash script that takes in a URL and displays all
curl -s -o /dev/null -w "%{http_code}" "$1"
