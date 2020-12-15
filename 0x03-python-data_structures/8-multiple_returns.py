#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        char = sentence[:1]
    return((length, char))