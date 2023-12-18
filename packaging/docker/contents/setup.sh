#!/bin/bash

set -e

echo "===== START DATABASE OPERATIONS ====="
echo "Running migrations..."
python manage.py migrate
echo
echo
echo "===== CREATING SUPERUSER... ====="
python manage.py createsuperuser --noinput
