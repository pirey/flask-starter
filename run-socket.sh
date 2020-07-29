#!/bin/bash

source ./.env
source ./.flaskenv

gunicorn --workers 3 --bind unix:jobsg.sock -m 007 jobsg:app
