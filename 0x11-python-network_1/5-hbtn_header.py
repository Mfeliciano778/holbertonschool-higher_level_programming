#!/usr/bin/python3
'''Task 1'''
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    body = requests.get(url)
    print(body.headers.get("X-Request-Id"))
