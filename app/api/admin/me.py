from flask import jsonify, request

from app import schemas as s
from app.lib import admin

from . import auth


def init_app(app):
    @app.route('/admin/me', methods=['GET'])
    @auth.authenticate_admin
    def get_me(admin_user):
        return jsonify(s.admin_user.dump(admin_user))
