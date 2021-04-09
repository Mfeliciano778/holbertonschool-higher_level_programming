#!/usr/bin/python3
'''Task 2'''
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as r:
            body = r.read()
        print(body.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
    
