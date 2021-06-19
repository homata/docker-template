#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# ex. Here is a list of commands you want to run after PostgreSQL is started.
python3 manage.py flush --no-input
python3 manage.py migrate
# python manage.py init_data

exec "$@"
