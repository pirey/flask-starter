#!/bin/bash

source ./.env
source ./.flaskenv

gunicorn --workers 3 --bind unix:app.sock -m 007 "app:create_app()"
