#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    # Catching every object of type Exception in a single except block is
    # actually dangerous, don't do this.
    except Exception as ex:
        stderr.write("Exception: {}\n".format(ex))
        return None
