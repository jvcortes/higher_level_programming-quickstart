#!/usr/bin/python3
"""
Makes a HTTP GET request to http://swapi.co/api/people/ with the
parameter "search" as the first argument.
"""
if __name__ == '__main__':
    import requests
    import sys

    request = requests.get("http://swapi.co/api/people/",
                           params={'search': sys.argv[1]})
    print("Number of results: {}".format(request.json()
                                         ['count']))

    while True:
        for ch in request.json()['results']:
            print(ch['name'])
        if request.json()["next"]:
            request = requests.get(request.json()['next'])
        else:
            break
