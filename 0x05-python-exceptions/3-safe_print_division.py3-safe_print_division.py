#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div_val = a / b
    except (ZeroDivisionError, FloatingPointError):
        div_val = None
    finally:
        print("Inside result: {}".format(div_val))
    return div_val
