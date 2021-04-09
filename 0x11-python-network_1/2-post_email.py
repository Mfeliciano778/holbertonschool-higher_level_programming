#!/usr/bin/python3
'''Task 2'''
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    url = argv[1]
    parsed = parse.urlencode({'email': email})
    data = parsed.encode('ascii')
    with request.urlopen(url, data) as r:
        body = r.read()
    print(body.decode('utf-8'))
