#!/bin/bash
#Bash script that sends a DELETE request to the URL 
#passed as the first argumen

curl -sX DELETE "$1"
