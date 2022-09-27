#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve the given challenge
"""
if __name__ == '__main__':
    import requests
    from sys import argv


    url = 'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
