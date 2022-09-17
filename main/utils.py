from flask import json


def load_json() -> list[dict]:
    """return a list of json objects"""
    with open('./data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_posts(search: str) -> list[dict]:
    """return a list of posts found by search"""
    posts = []
    for post in load_json():
        hashtags = []
        for word in post['content'].split():
            if word.startswith('#'):
                hashtags.append(word.split('#')[1].split('!')[0].lower())
        if search.lower() in hashtags:
            posts.append(post)
    return posts
