#!/usr/bin/python3
'''Task 4'''
import requests

if __name__ == "__main__":
    body = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
