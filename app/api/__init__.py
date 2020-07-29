import json
from app.api import admin, common
from app.logger import logger


def init_app(app):
    admin.init_app(app)
    common.init_app(app)
