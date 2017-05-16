release: python millenium_falcon/manage.py migrate
web: gunicorn --pythonpath millenium_falcon millenium_falcon.wsgi --log-file -