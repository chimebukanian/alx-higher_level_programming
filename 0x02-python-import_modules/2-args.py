#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no = len(sys.argv)
    if no == 1:
        print("{} arguments.".format(no - 1))
    elif no == 2:
        print("{} argument:".format(no - 1))
    else:
        print("{} arguments:".format(no - 1))

    for i in range(1, no):
        print("{}: {}".format(i, sys.argv[i]))
