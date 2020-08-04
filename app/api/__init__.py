import json
from flask_smorest import Api

from app.api import admin, common
from app.logger import logger

def create_api(app):
    app.config['API_TITLE'] = 'APP NAME'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.2'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_REDOC_PATH'] = '/redoc'
    app.config['OPENAPI_REDOC_URL'] = 'https://rebilly.github.io/ReDoc/releases/latest/redoc.min.js'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/docs'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/'
    app.config['API_SPEC_OPTIONS'] = {
            'security': [{'access_token': []}],
            'components': {
                'securitySchemes': {
                    'access_token': {
                        'type': 'apiKey',
                        'in': 'header',
                        'name': 'x-access-token',
                        }
                    }
                }
            }
    api = Api(app)
    return api

def init(app):
    api = create_api(app)

    admin.init(app, api)
    common.init(app, api)
