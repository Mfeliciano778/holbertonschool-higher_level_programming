#!/usr/bin/python3
'''Task 8'''
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    data = {'q': q}
    try:
        body = requests.post(url, data).json()
    except:
        print("Not a valid JSON")
    else:
        if body != "{}":
            print("[{}] {}".format(body.get("id"), body.get("name")))
        else:
            print("No result")
