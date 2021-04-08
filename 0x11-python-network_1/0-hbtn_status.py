#!/usr/bin/python3
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/projects/300') as r:
        body = r.read()
    print("Body response:")
    print("     - type: {}".format(type(body)))
    print("     - content: {}".format(body))
    print("     - utf8 content: {}".format(body.decode('utf-8')))
