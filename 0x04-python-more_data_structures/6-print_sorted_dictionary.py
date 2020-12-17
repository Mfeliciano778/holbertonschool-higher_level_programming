#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary.keys())
    for j in range(0, len(key)):
        print("{}: {}".format(key[j], a_dictionary.get(key[j])))
