web: gunicorn aqueous-savannah-13298..wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate