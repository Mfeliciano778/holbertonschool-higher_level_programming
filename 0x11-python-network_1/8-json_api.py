#!/usr/bin/python3
'''Task 8'''
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 1:
        q = ""
    else:
        q = argv[1]
    data = {"q": q}
    try:
        body = requests.post(url)
        json_rep = body.json()
        if json_rep != "{}":
            print("[{}] {}".format(json_rep.get("id"), json_rep.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
