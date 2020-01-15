#!/usr/bin/python3
"""
Makes a HTTP GET request to the first provided argument and retrieves the
header "X-Request-Id" using requests.Request
"""
if __name__ == '__main__':
    import requests

    request = requests.get("https://intranet.hbtn.io/status")
    if "X-Request-Id" in request.headers:
        print(request.headers["X-Request-Id"])
