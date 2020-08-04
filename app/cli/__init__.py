import os
import base64
import subprocess
import click
from app import db
from app.workflow import admin


def init(app):
    @app.cli.command('db:reset', short_help="Clear database, then init database.")
    def reset_db_command():
        from app import models

        try:
            db.reset_db()
            print('ok')
        except Exception as e:
            print(e)
            print('not ok')

    @app.cli.command('gen:key', short_help="Generate secret key.")
    def generate_key():
        random_bytes = os.urandom(64)
        key = base64.b64encode(random_bytes).decode('utf-8')
        print(key)

    @app.cli.command('test', short_help="Run tests")
    def run_tests():
        # TODO pass argument to run-test.sh script
        script = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'run-test.sh'
        )
        subprocess.run([script])

    @app.cli.command('gen:admin', short_help="Generate admin user")
    @click.argument('username')
    @click.argument('password')
    def generate_admin_user(username, password):
        admin.create_admin_user(username, password)
        print('admin user created')

    return app
