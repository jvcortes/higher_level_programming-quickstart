#!/usr/bin/python3
"""
Makes a HTTPS POST request to the first provided argument with an email
variable, provided with the second argument.
"""
if __name__ == '__main__':
    import sys
    from urllib import request, parse

    req = request.Request(sys.argv[1],
                          data=parse.urlencode(
                              {'email': sys.argv[2]}).encode())
    with request.urlopen(req) as response:
        contents = response.read()
        print(contents.decode())
