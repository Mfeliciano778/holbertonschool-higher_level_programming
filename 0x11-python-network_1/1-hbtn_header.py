#!/usr/bin/python3
'''Task 1'''
from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as r:
        body = r.info()
    print(body.get("X-Request-Id"))
