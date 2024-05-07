#!/usr/bin/python3

"""
    REDDIT API QUERY
"""

import requests

def top_ten(subreddit):
    """ MAIN """
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            resp = get_data.get("data")
            title = resp.get("title")
            print(title)
    return 0
