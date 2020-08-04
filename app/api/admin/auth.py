import jwt
from jwt.exceptions import InvalidTokenError
from functools import wraps
from flask import request, jsonify
from flask_smorest import Blueprint, abort
from app import config, schemas as s, models as m
from app.logger import logger
from app.workflow import admin


def authenticate_admin(f):
    @wraps(f)
    def _authenticate_admin(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            logger.error('Missing token %s' % token)
            return abort(401, message='Token is missing!')
            #  return {'message': 'Token is missing!'}, 401

        try:
            data = jwt.decode(token, config.SECRET_KEY)
            admin_user = m.AdminUser.query.get(data['id'])
        except InvalidTokenError:
            logger.error('Invalid token %s' % token)
            return abort(401, message='Token is invalid!')
            #  return {'message': 'Token is invalid!'}, 401
        except Exception as e:
            logger.error('Unknown authentication error %s' % e)
            return abort(401, message='Unknown error')
            #  return {'message': 'Unknown error'}, 401

        return f(admin_user, *args, **kwargs)

    return _authenticate_admin

def init(app, api):
    bp = Blueprint('Admin Auth', 'admin_auth', url_prefix='/admin/auth', description='auth for admin')

    @bp.route('/login', methods=['POST'])
    @bp.arguments(s.admin_user_login)
    @bp.response(s.admin_user_login_response, code=201)
    def login(payload):
        logger.info('login payload %s', payload)
        try:
            auth = admin.authenticate(**payload)
            token = auth['token']
            admin_user = s.admin_user.dump(auth['admin_user'])
            return {'token': token, 'admin_user': admin_user}
        except admin.InvalidCredentials:
            return abort(401, message='Invalid credentials.')

    @bp.route('/me', methods=['GET'])
    @bp.response(s.admin_user)
    @authenticate_admin
    def get_me(admin_user):
        return jsonify(s.admin_user.dump(admin_user))

    api.register_blueprint(bp)
