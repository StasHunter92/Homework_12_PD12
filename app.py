from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route('/uploads/<path:path>')
def static_uploads(path: str):
    """configure directory for uploaded files"""
    return send_from_directory('uploads', path)


if __name__ == '__main__':
    app.run(debug=True)
