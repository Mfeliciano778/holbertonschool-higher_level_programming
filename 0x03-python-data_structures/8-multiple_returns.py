#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        char = sentence[:1]
    else:
        char = None
    return((length, char))
