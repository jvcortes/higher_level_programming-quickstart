#!/usr/bin/python3
def magic_string():
    magic_string.c = getattr(magic_string, "c", []) + ["Holberton"]
    return ", ".join(magic_string.c)
