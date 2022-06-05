#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    if len(sentence) == 0:
        tup = 0, "None"
    else:
        tup = len(sentence), sentence[0]
    return tup
