#!/usr/bin/env bash

#apt-get remove python-django
#apt-get install python-mysqldb

#pip install --upgrade Django
echo 'Django version'
python -c "import django; print(django.get_version())"
#echo 'Django installation path'
#python -c "import django; print(django.__path__)"

rm -f /etc/nginx/sites-enabled/default 

rm -f /etc/gunicorn.d/test
ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test

rm -f /etc/gunicorn.d/ask
ln -sf /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/ask
/etc/init.d/gunicorn restart

ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
