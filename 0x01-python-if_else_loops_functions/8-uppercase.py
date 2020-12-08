#!/usr/bin/python3
def uppercase(str):
    char = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 123:
            c = ord(c) - 32
            char = char + chr(c)
        else:
            char = char + c
    print(char)
