#!/usr/bin/python3
'''Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
'''
import requests


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers'''
    url =  f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url)
    print(f'res code {res.status_code}')
    if res.status_code != 200:
        return 0
    else:
        return len(res.json()['data']['subscribers'])
