#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return None

    result = 0
    charset = {'M': 1000,
               'D': 500,
               'C': 100,
               'L': 50,
               'X': 10,
               'V': 5,
               'I': 1}
    prev = ''

    for c in reversed(roman_string):
        if c not in charset.keys():
            return None

        if prev in ('M', 'D') and c == 'C':
            result -= charset[c]
        elif prev in ('C', 'L') and c == 'X':
            result -= charset[c]
        elif prev in ('X', 'V') and c == 'I':
            result -= charset[c]
        else:
            result += charset[c]
        prev = c

    return result
