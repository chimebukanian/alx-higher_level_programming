#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the body of the response.
"""


if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    data = r.data
    print("Body response:")
    print(f'\t- type: {type(data)}')
    print(f'\t- content: {data}')
