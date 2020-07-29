from app.lib import admin


def test_authenticate_invalid_credentials(client):
    payload = {
        'username': 'bob',
        'password': 'password'
    }
    r = client.post('/admin/login', json=payload)
    assert r.status_code == 401
    assert r.get_json() == {
        'message': 'Invalid credentials.', 'type': 'login_error'}


def test_authenticate(client):
    admin.create_admin_user('bob', 'password')

    payload = {
        'username': 'bob',
        'password': 'password'
    }
    r = client.post('/admin/login', json=payload)
    auth = r.get_json()
    assert r.status_code == 200
    assert auth['token'] is not None
    assert auth['token'] != ''
