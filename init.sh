#! /bin/bash

easy_install -m
rm -rf /usr/lib/python2.7/dist-packages/Django-1.6.1.egg-info
rm -rf /usr/lib/python2.7/dist-packages/django

pip install --upgrade Django
echo 'Python version'
python -c "import django; print(django.get_version())"
echo 'Python path'
python -c "import django; print(django.__path__)"

rm -f /etc/nginx/sites-enabled/default 
ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
rm -f /etc/gunicorn.d/test

ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test

rm -f /etc/gunicorn.d/ask
ln -sf /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/ask
/etc/init.d/gunicorn restart
