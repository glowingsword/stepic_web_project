#!/usr/bin/env bash

rm -f /home/box/web/ask/db.sqlite3
cd /home/box/web/ask; python manage.py syncdb
chmod 666 /home/box/web/ask/db.sqlite3
chmod 777 /home/box/web/ask/
