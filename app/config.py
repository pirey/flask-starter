import os

FLASK_ENV = os.getenv('FLASK_ENV', 'production')
SECRET_KEY = os.environ['SECRET_KEY']
DATABASE_URL = os.environ['DATABASE_URL']

def init(app):
    app.config['SECRET_KEY'] = SECRET_KEY
