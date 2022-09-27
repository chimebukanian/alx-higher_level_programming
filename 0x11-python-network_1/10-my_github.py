#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv


    url = f'https://api.github.com/users/{argv[1]}'
    r = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
