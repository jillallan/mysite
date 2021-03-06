import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    @app.route('/')
    def hello():
        return "Hello world"

    print(os.environ['APP_SETTINGS'])

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass       

    return app