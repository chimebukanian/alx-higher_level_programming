#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return None
    big = max(a_dictionary.values())
    return [k for k, v in a_dictionary.items() if big == v][0]
