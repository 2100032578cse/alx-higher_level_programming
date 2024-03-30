#!/bin/bash
#Bash script that takes in a URL and displays all
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
