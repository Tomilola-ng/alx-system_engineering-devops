#!/usr/bin/python3

"""
    REDDIT API QUERY
"""

import requests

def recurse(subreddit, hot_list=[], after=""):
    """ MAIN """
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = response.json().get("data").get("after")

        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    return 0
