#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn book_my_movie.wsgi:application --bind 0.0.0.0:8000