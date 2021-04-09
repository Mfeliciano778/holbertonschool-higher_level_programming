#!/usr/bin/python3
'''Task 2'''
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        body = requests.get(url)
        body.raise_for_status()
        print(body.text)
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(requests.get(url).status_code))
