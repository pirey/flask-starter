import pytest
import jwt
from faker import Faker
from faker.providers import internet
from datetime import date, datetime, timedelta
from werkzeug.security import generate_password_hash
from app import create_app, models as m, config, db

fake = Faker()
fake.add_provider(internet)

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    db.reset_db()
    with app.test_client() as client:
        yield client


@pytest.fixture
def admin_user():
    """Get first admin user in the db, or create one if not exists"""
    hashed_password = generate_password_hash('password', method='sha256')
    _admin_user = m.AdminUser.query.first()
    if _admin_user is None:
        _admin_user = m.AdminUser(username='admin',
                                       password=hashed_password,
                                       status=m.ADMIN_USER_ACTIVE)
        db.session.add(_admin_user)
        db.session.commit()
    return _admin_user


@pytest.fixture
def admin_token(admin_user):
    token = jwt.encode({'id': admin_user.id, 'exp': datetime.utcnow(
    ) + timedelta(minutes=30)}, config.SECRET_KEY)
    return token.decode('utf-8')


@pytest.fixture
def admin_auth_headers(admin_token):
    return {'x-access-token': admin_token}
