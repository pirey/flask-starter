from app.workflow import admin


def test_get_me_without_auth(client):
    r = client.get('/admin/me')
    assert r.status_code == 401
    assert r.get_json() == {'message': 'Token is missing!'}


def test_get_me(client, admin_user, admin_auth_headers):
    r = client.get('/admin/me', headers=admin_auth_headers)
    admin_user_json = r.get_json()
    assert r.status_code == 200
    assert admin_user_json['id'] == admin_user.id
    assert admin_user_json['username'] == admin_user.username
    assert admin_user_json['status'] == admin_user.status

