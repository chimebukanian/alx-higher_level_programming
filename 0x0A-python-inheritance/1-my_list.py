#!/usr/bin/python3
""" My task 1 module """


class MyList(list):
    """ MyList Class """
    def print_sorted(self):
        """ Ascending sort function """
        res = sorted(self)
        print(res)
