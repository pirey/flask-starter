import os

from datetime import datetime
from flask import Flask
from flask_cors import CORS

from app.logger import logger
from app import config, db, cli, api

# TODO params to override some config
def create_app():
    app = Flask(__name__)


    config.init(app)
    cli.init(app)
    api.init(app)
    db.init(app)

    CORS(app)

    return app
