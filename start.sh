#!/bin/bash
echo start script BEGINS
ls
pwd
fuser -k 8000/tcp
sleep 5
nohup python3 /root/manage.py runserver 0.0.0.0:8000 &
