#!/usr/bin/python3
"""
Makes a HTTP POST request to http://0.0.0.0:5000/search_user with the POST
value q if provided as the first argument.
"""
if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    try:
        request = requests.post("http://0.0.0.0:5000/search_user",
                                data={'q': q})
        if not request.text or not request.json():
            print("No result")
        else:
            print("[{}] {}".format(request.json()['id'],
                                   request.json()['name']))
    except ValueError:
        print("Not a valid JSON")
