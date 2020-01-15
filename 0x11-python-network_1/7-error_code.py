#!/usr/bin/python3
"""
Makes a HTTP GET request to a provided URL, displays error code instead
if present.
"""
if __name__ == '__main__':
    import requests
    import sys

    request = requests.get(sys.argv[1])
    if request.status_code < 400:
        print(request.text)
    else:
        print("Error code: {}".format(request.status_code))
