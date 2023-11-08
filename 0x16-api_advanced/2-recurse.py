#!/usr/bin/python3
'''recursive function returns titles of all hot articles of a subreddit'''
import requests


def recurse(subreddit, hot_list=[]):
    ''' a recursive function that queries the Reddit API '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    res = requests.get(url)
    if res.status_code == 200:
        all_data = res.json()['data']
        if all_data:
            for data in all_data:
                hot_list.append(data['title'])
        if len(all_data) > 10:
            hot_list.extend(recurse(subreddit, hot_list))
        return hot_list
    else:
        return None
