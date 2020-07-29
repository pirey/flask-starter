#!/bin/bash


# TODO find a way to be able to run test for CI
source ./.env.testing
source ./.flaskenv

coverage run --omit '.venv/*' -m pytest --timeout=10 --disable-warnings "$@"

# TODO allow cli argument to genrate coverage
# to generate coverage report, run:
# coverage html
