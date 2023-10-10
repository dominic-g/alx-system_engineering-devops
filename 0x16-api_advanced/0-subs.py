#!/usr/bin/python3
"""
Python function that utilizes the Reddit API to retrieve the
total number of subscribers (excluding active users) for
a specified subreddit. If an invalid subreddit is provided,
the function returns 0..
"""
import requests


def number_of_subscribers(subreddit):
    link = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) \
        Gecko/20100101 Firefox/105.0'
    }

    res = requests.get(link, headers=headers)
    data = res.json()
    if res.status_code == 200:
        return data['data']['subscribers']
    elif res.status_code == 404:
        return 0
