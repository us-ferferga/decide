#!/bin/bash

## This script finishes the installation of the devcontainer
##
## Currently it just sets up the database user using decide's local_settings.py default values
## If you want to modify those credentials,
## you can alter them at any time manually: https://stackoverflow.com/questions/12720967/how-can-i-change-a-postgresql-user-password

su - postgres <<EOSQL
psql -c "create user decide with password 'decide'"
psql -c "create database decide owner decide"
EOSQL

echo "127.0.0.1 db" >> /etc/hosts
