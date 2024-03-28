#!/bin/bash
# Get the byte size of the HTTP response header for a given URL
size=$(curl -sI "$url" | grep -i "Content-Length" | cut -d ' ' -f2)
