#!/bin/bash
# Get the byte size of the HTTP response header for a given URL

url=$1
size=$(curl -sI "$url" | grep -i "Content-Length" | cut -d ' ' -f2)
echo "$size"
