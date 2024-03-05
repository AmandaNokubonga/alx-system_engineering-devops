#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """ Print first 10 titles """
    if subreddit is None or type(subreddit) is not str:
        return None

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'chrome:0x16-api_advanced:v1'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
        }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    response = response.json().get('data')
    after = response.get('after')
    count = response.get('dist')
    [hot_list.append(c.get('data').get('title'))
     for c in response.get('children')]

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
