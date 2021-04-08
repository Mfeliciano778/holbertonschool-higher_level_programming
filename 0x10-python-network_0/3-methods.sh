#!/bin/bash
# displays all methods of url
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-11
