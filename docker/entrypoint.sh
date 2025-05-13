#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

echo "Rebuilding search index..."
yes | python manage.py search_index --rebuild

echo "Starting Gunicorn server..."
exec gunicorn shop.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120
