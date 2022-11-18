#!/bin/sh

if [[ $1 == 'start' ]]; then
  sudo lsof -t -i tcp:8000 | xargs kill -9
  python manage.py runserver
fi

if [[ $1 == 'init' ]]; then
  python -m venv .venv
  # shellcheck disable=SC2039
  source ./.venv/bin/activate
  python -m pip install python-dotenv
  pip install djangorestframework
  pip install psycopg2-binary
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python load_data.py
  python manage.py runserver
fi

if [[ $1 == 'stop' ]]; then
  sudo lsof -t -i tcp:8000 | xargs kill -9
  sudo lsof -t -i tcp:5432 | xargs kill -9
fi