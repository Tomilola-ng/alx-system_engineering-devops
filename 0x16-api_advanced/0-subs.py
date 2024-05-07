#!/usr/bin/python3

"""
    REDDIT API QUERY
"""

import requests

def number_of_subscribers(subreddit):
    """ MAIN """
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={"User-Agent": "Custom"},
    )

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
