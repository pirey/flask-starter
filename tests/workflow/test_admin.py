import pytest
from app import models as m
from app.workflow import admin


def test_create_admin_user(reset_db):
    admin_user = admin.create_admin_user('bob', 'password')
    assert admin_user.username == 'bob'
    assert admin_user.status == m.ADMIN_USER_ACTIVE


def test_authenticate(reset_db):
    admin_user = admin.create_admin_user('bob', 'password')
    auth = admin.authenticate('bob', 'password')
    assert auth['token'] is not None
    assert auth['token'] != ''
    assert auth['admin_user'] == admin_user


def test_authenticate_invalid_credentials(reset_db):
    with pytest.raises(admin.InvalidCredentials):
        admin.create_admin_user('bob', 'password')
        admin.authenticate('wrong', 'password')
        admin.authenticate('bob', 'wrong')
