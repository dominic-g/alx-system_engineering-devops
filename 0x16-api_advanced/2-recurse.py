#!/usr/bin/python3
"""
Python recursive function that interacts with the Reddit API.
This function retrieves a list containing the titles of
all hot articles from a specified subreddit. If there are no
articles found for the given subreddit,
the function returns None
"""
import requests


def recurse(subreddit, hot_list=[], af=''):
    """reurcse function to get response from Reddit API"""
    lk = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, af)
    headers = {
        'User-agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) \
        Gecko/20100101 Firefox/105.0'
    }

    res = requests.get(lk, headers=headers, allow_redirects=False)

    if res.status_code == 404:
        return None

    data = res.json()
    if res.status_code == 200:
        for element in data['data']['children']:
            hot_list.append(element['data']['title'])
    af = data['data']['after']

    if af is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, af)
