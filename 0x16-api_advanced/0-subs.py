#!/usr/bin/python3
'''function that queries the Reddit API and returns the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url)
    print(f'res code {res.status_code}')
    if res.status_code != 200:
        return 0
    else:
        return res.json()['data']['subscribers']
