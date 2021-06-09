#!/bin/bash
echo migrate script BEGINS
ls
pwd
pip3 install -r /root/requirements.txt
python3 /root/manage.py makemigrations && python3 /root/manage.py migrate
