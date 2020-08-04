from app.workflow import admin
from app.logger import logger


def test_authenticate_invalid_credentials(client):
    payload = {
        'username': 'bob',
        'password': 'password'
    }
    r = client.post('/admin/auth/login', json=payload)
    logger.info('json %s', r.get_json())
    assert r.status_code == 401
    assert r.get_json()['message'] == 'Invalid credentials.'

def test_authenticate_validates_request(client):
    # TODO
    pass

def test_authenticate(client):
    admin.create_admin_user('bob', 'password')

    payload = {
        'username': 'bob',
        'password': 'password'
    }
    r = client.post('/admin/auth/login', json=payload)
    auth = r.get_json()
    assert r.status_code == 201
    assert auth['token'] is not None
    assert auth['token'] != ''

def test_get_me_without_auth(client):
    r = client.get('/admin/auth/me')
    assert r.status_code == 401
    assert r.get_json()['message'] == 'Token is missing!'


def test_get_me(client, admin_user, admin_auth_headers):
    r = client.get('/admin/auth/me', headers=admin_auth_headers)
    admin_user_json = r.get_json()
    assert r.status_code == 200
    assert admin_user_json['id'] == admin_user.id
    assert admin_user_json['username'] == admin_user.username
    assert admin_user_json['status'] == admin_user.status

