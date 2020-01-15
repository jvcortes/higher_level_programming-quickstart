#!/usr/bin/python3
"""
Makes a HTTP POST request to https://api.github.com/repos with the repo owner
as the first argument and the repo name as the second argument.
"""
if __name__ == '__main__':
    import requests
    import sys

    request = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2],
        sys.argv[1]
    ))
    for commit in request.json()[:10]:
        print("{}: {}".format(commit['sha'],
                              commit['commit']['author']['name']))
