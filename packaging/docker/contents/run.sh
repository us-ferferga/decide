#!/bin/bash

set -e

echo "Starting Decide..."
echo ""
echo ""
exec python manage.py runserver 0.0.0.0:80
