web: gunicorn uuportal.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=uuportal --loglevel=info
