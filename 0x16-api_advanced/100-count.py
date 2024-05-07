#!/usr/bin/python3

"""
    REDDIT API QUERY
"""

import random
import requests

def count_words(subreddit, word_list, word_count=[], page_after=None):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    if not subreddit or not word_list:
        print("Error: Subreddit and word list must be non-empty.")
        return

    user_agent = 'MyUserAgent/{}.{}.{}'.format(
        random.randint(1, 999),
        random.randint(1, 999),
        random.randint(1, 999)
    )
    headers = {'User-Agent': user_agent}

    word_list = [word.lower() for word in word_list]
    word_count_dict = dict.fromkeys(word_list, 0)

    def process_page(subreddit, word_count_dict, after=None):
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        if after:
            url += f'?after={after}'

        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for child in data['data']['children']:
                for word in word_count_dict:
                    word_count_dict[word] += sum(
                        1 for title_word in child['data']['title'].split() if title_word.lower() == word
                    )

            if data['data']['after']:
                process_page(subreddit, word_count_dict, data['data']['after'])
            else:
                for word, count in sorted(word_count_dict.items(), key=lambda x: (-x[1], x[0])):
                    if count > 0:
                        print(f'{word}: {count}')

    process_page(subreddit, word_count_dict)
