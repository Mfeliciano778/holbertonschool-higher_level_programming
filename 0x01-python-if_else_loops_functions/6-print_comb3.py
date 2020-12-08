#!/usr/bin/python3
for tens in range(0, 10):
    for ones in range(1, 10):
        if tens == ones or ones < tens:
            pass
        elif tens == 8 and ones == 9:
            print("{:d}{:d}".format(tens, ones))
        else:
            print("{:d}{:d}".format(tens, ones), end=", ")
