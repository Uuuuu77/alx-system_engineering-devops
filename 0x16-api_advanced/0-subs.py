#!/usr/bin/python3

"""
    Query the Reddit API and returns number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Query API to return number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'john'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
