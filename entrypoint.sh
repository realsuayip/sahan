#!/bin/sh

while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
  sleep 0.1
done

python manage.py collectstatic --noinput
python manage.py migrate --noinput
exec "$@"
