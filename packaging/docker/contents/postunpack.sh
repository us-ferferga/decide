#!/bin/bash

set -e

mkdir -p /data
rm -rf /bin/sh
ln -s /bin/bash /bin/sh
ln -s /data /app/decide/data
rm -rf /scripts/prebuild.sh
mv /scripts/docker-settings.py /app/decide/local_settings.py
pip install -r /app/requirements.txt
rm -rf /root/.cache
