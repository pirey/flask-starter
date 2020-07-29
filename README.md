# Flask project starter

Solid starter for rapid flask project.

## Requirements

- python 3.8.5
- virtualenv
- see `requirements.txt` and `requirements-dev.txt` for more

## Project Overview

**TODO**

## Setup

- `git clone`
- `virtualenv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install -r requirements-dev.txt`
- `cp .env.example .env`
- Edit `.env`

You may want to rename `app` module to name of the project.

## Development

`flask run`.

**NOTE** the command above is only for development purpose, see deployment guide below on how to run the app for production.

## Testing

- `cp .env .env.testing`
- Edit `.env.testing`

To run test, use `flask test`

## Available Commands

To see available commands, run:

`flask --help`

### Deploy with docker

**TODO**

### Deploy manually (Ubuntu 18.04)

Use nginx to handle request, and proxy the request to gunicorn process (started via systemd unit file).

- `sudo apt install nginx python3-pip postgresql postgresql-client libpq-dev`
    - NOTE: postgresql is required for psycopg2 library to work, regardless of where we store our database
- `pip3 install virtualenv`
- `git clone {repo_url} {project_dir}`
- `cd {project_dir}`
- `rm -rf .git`
- `virtualenv .venv`
- `source .venv/bin/activate`
- `pip3 install -r requirements.txt`
- edit config files inside `deploy` folder appropriately
    - `cp {project_dir}/deployment/app-server.service /etc/systemd/system`
    - `cp {project_dir}/deployment/app-server.conf /etc/nginx/conf.d`
- start services
    - `systemctl enable --now app-server`
    - `systemctl restart nginx`
