#!/bin/sh
rm db.sqlite3
rm -r cforums/migrations/
rm -r cforums/__pycache__

python manage.py migrate --fake cforums zero
python manage.py makemigrations cforums
python manage.py migrate cforums
python manage.py migrate
