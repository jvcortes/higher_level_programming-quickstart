#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = str[:n] + str[n + 1:]
    return cpy
