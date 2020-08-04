import os

from datetime import datetime
from flask import Flask
from flask_cors import CORS

from app.logger import logger
from app import config, db, cli, api

# TODO params to override some config
def create_app():
    app = Flask(__name__)


    config.init_app(app)
    cli.init_app(app)
    api.init_app(app)
    db.init_app(app)

    CORS(app, support_credentials=True)

    return app
