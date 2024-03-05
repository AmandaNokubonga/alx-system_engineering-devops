#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Print first 10 titles """
    if subreddit is None or type(subreddit) is not str:
        return None

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'chrome:0x16-api_advanced:v1'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print('None')
        return

    response = response.json()
    title = response.get('data')
    [print(c.get('data').get('title')) for c in title.get('children')]
