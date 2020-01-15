#!/usr/bin/python3
"""
Makes a HTTP GET request to https://intranet.hbtn.io/status using
requests.Request.
"""
if __name__ == '__main__':
    import requests

    request = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n"
          "\t- type: {}\n"
          "\t- content: {}".format(type(request.text),
                                   request.text))
