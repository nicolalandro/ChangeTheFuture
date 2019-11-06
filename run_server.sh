#!/bin/bash

python back_end/manage.py migrate
gunicorn --pythonpath back_end app.wsgi
