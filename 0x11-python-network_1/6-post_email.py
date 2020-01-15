#!/usr/bin/python3
"""
Makes a HTTP POST request with an 'email', using the second provided argument
value to the first provided argument (url) and retrieves the response body.
"""
if __name__ == '__main__':
    import requests
    import sys

    request = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(request.text)
