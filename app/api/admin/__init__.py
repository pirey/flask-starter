from .auth import authenticate_admin
from . import auth
from . import me

def init_app(app):
    # TODO use route prefix
    auth.init_app(app)
    me.init_app(app)
