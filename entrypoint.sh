./manage.py migrate;
./manage.py compilemessages;
./manage.py collectstatic --noinput;
gunicorn --bind=0.0.0.0:8000 --timeout=90 --workers=6 --preload web.wsgi:application;
