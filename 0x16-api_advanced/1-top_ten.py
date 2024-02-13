#!/usr/bin/python3
"""
    Queries the Reddit API and returns number of subscribers.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'john'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
