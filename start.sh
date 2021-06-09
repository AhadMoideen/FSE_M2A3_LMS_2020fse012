#!/bin/bash
fuser -k 8000/tcp
sleep 5
nohup python3 ./manage.py runserver 0.0.0.0:8000 &
