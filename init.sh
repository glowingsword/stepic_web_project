#! /bin/bash
rm -f /etc/nginx/sites-enabled/default 
ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
rm -f /etc/gunicorn.d/test

ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test

rm -f /etc/gunicorn.d/ask
ln -sf /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/ask
/etc/init.d/gunicorn restart
