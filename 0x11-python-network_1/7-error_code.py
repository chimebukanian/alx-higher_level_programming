#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL 
and displays the bodyof the response.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    try:
        r = requests.get(f'{url}')
        print(r.text)
    except HTTPError as e:
        print('Error code: {r.status_code}')
