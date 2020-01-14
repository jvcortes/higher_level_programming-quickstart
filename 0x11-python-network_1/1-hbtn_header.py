#!/usr/bin/python3
"""
HTTPS Requests to the first provided argument and retrieves the header
"X-Request-Id".
"""
if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
