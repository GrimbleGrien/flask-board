import os

from dotenv import load_dotenv
from flask import Flask
from board import pages

load_dotenv()

def create_app():
    app = Flask(__name__)
    # app.config.from_prefixed_env()

    # print(f"current env: {os.getenv('ENVIRONMENT')}")
    # print(f"using database: {app.config.get('DATABASE')}")
    app.register_blueprint(pages.bp)
    return app