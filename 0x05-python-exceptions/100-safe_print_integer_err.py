#!/usr/bin/python3
def safe_print_integer_err(val):
    import sys
    try:
        print("{:d}".format(val))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
