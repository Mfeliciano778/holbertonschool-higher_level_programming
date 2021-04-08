#!/bin/bash
# sends a post request and displays body
curl -sL -X "POST" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
