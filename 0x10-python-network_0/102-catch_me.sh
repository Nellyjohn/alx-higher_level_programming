#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -d "user_id=98" "0.0.0.0:5000/catch_me" -H "Origin:HolbertonSchool" -X PUT 
