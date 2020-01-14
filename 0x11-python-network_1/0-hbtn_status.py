#!/usr/bin/python3
"""
HTTPS Requests to intranet.hbtn.io/status and prints some basic information
"""
if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body response:\n"
              "\t- type: {}\n"
              "\t- content: {}\n"
              "\t- utf8 content: {}".format(type(content),
                                            content,
                                            content.decode()))
