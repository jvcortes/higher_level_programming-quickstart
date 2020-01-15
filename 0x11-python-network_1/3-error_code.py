#!/usr/bin/python3
"""
Makes a GET HTTP request to an URL provided by the first argument, if a HTTP
error occurs, the program will display its code instead.
"""
if __name__ == '__main__':
    import sys
    import urllib.request
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            contents = response.read()
            print(contents.decode())
    except HTTPError as e:
        print("Error code: {}".format(e.code))
