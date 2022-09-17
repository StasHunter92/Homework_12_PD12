from json import JSONDecodeError
from flask import Blueprint, render_template, request
from logs.loggers import logger_search, logger_json
from main.utils import search_posts

main_blueprint = Blueprint('main_blueprint', __name__,
                           template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """return the main page"""
    return render_template('index.html')


@main_blueprint.route('/search')
def post_list():
    """return the search results"""
    search: str = request.args.get('s')
    logger_search.info(f'Поиск по запросу "{search}"')
    try:
        result: list[dict] = search_posts(search)
    except FileNotFoundError:
        logger_json.error('Не удалось открыть файл')
        return f'Не удалось открыть файл'
    except JSONDecodeError:
        logger_json.error('Не удалось прочитать файл')
        return f'Не удалось прочитать файл'
    return render_template('post_list.html', search=search, result=result)
