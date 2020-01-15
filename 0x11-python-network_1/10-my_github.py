#!/usr/bin/python3
"""
Makes a HTTP POST request to https://api.github.com/user with the username
as the first argument and its password as the seconf argument.
"""
if __name__ == '__main__':
    import requests
    import sys

    request = requests.get("https://api.github.com/user", auth=(sys.argv[1],
                                                                sys.argv[2]))
    if "id" in request.json().keys():
        print(request.json()['id'])
    else:
        print("None")
