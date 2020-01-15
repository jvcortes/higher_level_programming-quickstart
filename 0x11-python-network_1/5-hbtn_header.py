#!/usr/bin/python3
"""
Makes a HTTP GET request to the first provided argument and retrieves the
header "X-Request-Id" using requests.Request
"""
if __name__ == '__main__':
    import requests
    import sys

    request = requests.get(sys.argv[1])
    if "X-Request-Id" in request.headers:
        print(request.headers["X-Request-Id"])
