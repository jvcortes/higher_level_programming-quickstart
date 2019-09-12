#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = 1

    if not sys.argv[1:]:
        print("0 arguments.")
    elif len(sys.argv[1:]) == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv[1:])))

    for element in sys.argv[1:]:
        print("{}: {}".format(i, element))
        i += 1
