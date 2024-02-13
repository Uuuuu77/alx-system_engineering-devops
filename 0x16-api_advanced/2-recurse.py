#!/usr/bin/python3
"""
    Queries the Reddit API and returns number of subscribers.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        Queries the Reddit API and returns a list containing
        the titles of all hot articles for a given subreddit
    """
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(
                subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
             subreddit, after)
    headers = {'User-Agent': 'john'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
    return hot_list if hot_list else None
