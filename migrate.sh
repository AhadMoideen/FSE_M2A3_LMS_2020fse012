#!/bin/bash
echo dependencies script BEGINS
pwd
pip3 install -r ./requirements.txt
python3 ./manage.py makemigrations && python3 ./manage.py migrate
