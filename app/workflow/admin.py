import jwt
import datetime as dt
from werkzeug.security import check_password_hash, generate_password_hash
from app import models, db, config
from app.logger import logger


class InvalidCredentials(Exception):
    pass


def authenticate(username, password, **ignore):
    admin_user = models.AdminUser.query.filter_by(username=username).first()

    if not admin_user:
        raise InvalidCredentials()

    if check_password_hash(admin_user.password, password):
        exp = dt.datetime.utcnow() + dt.timedelta(minutes=30)
        token = jwt.encode(
            {'id': admin_user.id, 'exp': exp}, config.SECRET_KEY)

        return {'token': token.decode('UTF-8'), 'admin_user': admin_user}
    else:
        raise InvalidCredentials()


def create_admin_user(username, password):
    admin_user = models.AdminUser()
    admin_user.username = username
    admin_user.password = generate_password_hash(password, method='sha256')
    db.session.add(admin_user)
    db.session.commit()
    return admin_user
