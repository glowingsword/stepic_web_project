#!/usr/bin/env bash

mysql -uroot -e "create database ask;"
mysql -uroot -e "CREATE USER 'ask'@'localhost' IDENTIFIED BY 'Jocho4Za';"
mysql -uroot -e "GRANT ALL ON ask.* TO 'ask'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
