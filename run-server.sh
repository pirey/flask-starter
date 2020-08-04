#!/bin/bash

source ./.env
source ./.flaskenv

gunicorn "app:create_app()" --preload -b 0.0.0.0:${PORT:-5000}
