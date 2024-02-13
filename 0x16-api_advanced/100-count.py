#!/usr/bin/python3
"""
    Queries the Reddit API.
"""
import requests
from collections import defaultdict


def count_words(subreddit, word_list, after=None, counts=None):
    """
    queries the Reddit API, parses the title of all hot articles
    and prints a sorted count of given keywords
    """
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(
                subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
             subreddit, after)

    if counts is None:
        counts = defaultdict(int)

    headers = {'User-Agent': 'john'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            t = " {} ".format(title)

            for word in word_list:
                w = " {} ".format(word.lower())
                if w in t:
                    counts[word.lower()] += 1

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)

        sorted_counts = sorted(counts.items(),
                               key=lambda item: (-item[1], item[0]))

        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        return None
