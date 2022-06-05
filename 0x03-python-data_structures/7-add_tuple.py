#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_1st = tuple_a + (0, 0)
    tuple_2nd = tuple_b + (0, 0)
    new_tuple = tuple_1st[0] + tuple_2nd[0], tuple_1st[1] + tuple_2nd[1]
    return new_tuple
