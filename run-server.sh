#!/bin/bash

source ./.env
source ./.flaskenv

gunicorn app:app --preload -b 0.0.0.0:${PORT:-5000}
