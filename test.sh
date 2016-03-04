#!/bin/bash
wget -O- http://localhost/uploads/test.txt > test.log
wget -O- http://localhost/img/test.txt >> test.log
wget -O- http://localhost/public/img/ >> test.log
