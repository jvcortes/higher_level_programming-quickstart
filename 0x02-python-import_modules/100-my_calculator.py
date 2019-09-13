#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    if sys.argv[2] not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, *, /")
        exit(1)

    if sys.argv[2] == '+':
        print("{} + {} = {}".format(
            int(sys.argv[1]),
            int(sys.argv[3]),
            add(int(sys.argv[1]), int(sys.argv[3]))))
    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(
            int(sys.argv[1]),
            int(sys.argv[3]),
            sub(int(sys.argv[1]), int(sys.argv[3]))))
    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(
            int(sys.argv[1]),
            int(sys.argv[3]),
            mul(int(sys.argv[1]), int(sys.argv[3]))))
    elif sys.argv[2] == '/':
        if int(sys.argv[3]) == 0:
            print("Error. Division by zero")
            exit(1)
        else:
            print("{} / {} = {}".format(
                int(sys.argv[1]),
                int(sys.argv[3]),
                div(int(sys.argv[1]), int(sys.argv[3]))))
