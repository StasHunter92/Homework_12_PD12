from flask import Blueprint, render_template, request
from json import JSONDecodeError
from loader.utils import set_post_to_json, check_extension
from logs.loggers import logger_extensions, logger_json

loader_blueprint = Blueprint('loader_blueprint', __name__,
                             template_folder='templates')


@loader_blueprint.route('/post')
def post_form():
    """page with form to upload post"""
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_uploaded():
    """page after successful upload"""
    picture = request.files.get('picture')
    text: str = request.form.get('content')
    filename: str = picture.filename
    if not picture or not text:
        return f'Отсутствует картинка или описание'
    elif not check_extension(filename):
        logger_extensions.info(f"Попытка загрузки {filename.split('.')[-1]}")
        return f'Данный тип файлов "{filename.split(".")[-1]}" запрещен'
    else:
        try:
            path = f'./uploads/images/{filename}'
            set_post_to_json(path, text)
            picture.save(path)
        except FileNotFoundError:
            logger_json.error('Не удалось открыть файл')
            return f'Не удалось открыть файл'
        except JSONDecodeError:
            logger_json.error('Не удалось прочитать файл')
            return f'Не удалось прочитать файл'
    return render_template('post_uploaded.html', filename=filename, text=text)
