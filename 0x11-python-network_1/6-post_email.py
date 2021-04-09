#!/usr/bin/python3
'''Task 1'''
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    email2 = {"email": email}
    body = requests.post(url, email2)
    print(body.text)
