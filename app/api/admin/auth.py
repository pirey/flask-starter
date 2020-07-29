import jwt
from jwt.exceptions import InvalidTokenError
from functools import wraps
from flask import request
from app import config, schemas as s, models as m
from app.logger import logger
from app.lib import admin


def authenticate_admin(f):
    @wraps(f)
    def _authenticate_admin(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            logger.error('Missing token %s' % token)
            return {'message': 'Token is missing!'}, 401

        try:
            data = jwt.decode(token, config.SECRET_KEY)
            admin_user = m.AdminUser.query.get(data['id'])
        except InvalidTokenError:
            logger.error('Invalid token %s' % token)
            return {'message': 'Token is invalid!'}, 401
        except Exception as e:
            logger.error('Unknown authentication error %s' % e)
            return {'message': 'Unknown error'}, 401

        return f(admin_user, *args, **kwargs)

    return _authenticate_admin


def init_app(app):
    @app.route('/admin/login', methods=['POST'])
    def login():
        payload = s.admin_login.load(request.get_json())
        try:
            auth = admin.authenticate(**payload)
            token = auth['token']
            admin_user = s.admin_user.dump(auth['admin_user'])
            return {'token': token, 'admin_user': admin_user}
        except admin.InvalidCredentials:
            return {'message': 'Invalid credentials.', 'type': 'login_error'}, 401
