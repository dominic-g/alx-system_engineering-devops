#!/usr/bin/python3
"""
Function to print first 10 titles from subreddit
"""
import requests


def top_ten(subreddit):
    """Retrieves using the Reddit API"""
    link = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) \
        Gecko/20100101 Firefox/105.0'
    }

    res = requests.get(link, headers=headers, allow_redirects=False)
    data = res.json()
    if res.status_code == 200:
        for sub in data['data']['children']:
            print(sub['data']['title'])
    elif res.status_code == 404:
        print(None)
