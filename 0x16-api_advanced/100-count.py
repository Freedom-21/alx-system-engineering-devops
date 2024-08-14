#!/usr/bin/python3
"""
Module provides a recursive function to query the Reddit API,
parse the title of all hot articles, and print a sorted count of given keywords
"""

import requests

def count_words(subreddit, word_list, after=None, counts={}):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        posts = data['data']['children']
        
        if not posts and not counts:
            return
        
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title.split():
                    counts[word.lower()] = counts.get(word.lower(), 0) + title.split().count(word.lower())

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    except Exception:
        return
