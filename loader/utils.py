from flask import json
from main.utils import load_json

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


def set_post_to_json(image: str, description: str) -> None:
    """return a list of json objects"""
    data: list[dict] = load_json()
    with open('./data/posts.json', 'w', encoding='utf-8') as file:
        post = {
            'pic': image,
            'content': description,
        }
        data.append(post)
        json.dump(data, ensure_ascii=False, fp=file, indent=2)


def check_extension(filename: str) -> bool:
    """return extension is allowed"""
    extension: str = filename.split('.')[-1]
    return extension in ALLOWED_EXTENSIONS
