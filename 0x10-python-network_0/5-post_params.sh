#!/bin/bash
# curls to an URL through a HTTP POST request using some variables
curl -s -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
