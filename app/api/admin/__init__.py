from .auth import authenticate_admin
from . import auth

def init(app, api):
    auth.init(app, api)
