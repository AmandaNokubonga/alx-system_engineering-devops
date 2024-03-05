#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ function to check number of subscribers """
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'chrome:0x16-api_advanced:v1'}

    response = requests.get(url, headers=headers).json()
    subs = response.get('data', {}).get('subscribers', 0)
    return subs
