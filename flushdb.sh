#!/bin/sh
python manage.py migrate --fake cforums zero
python manage.py makemigrations cforums
python manage.py migrate cforums
python manage.py migrate
