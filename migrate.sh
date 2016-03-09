#!/usr/bin/env bash

cd /home/box/web/ask; python manage.py makemigrations; python manage.py migrate
