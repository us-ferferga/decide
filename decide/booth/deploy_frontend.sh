#!/bin/bash

rm -rf frontend/dist
npm -w @decide/booth ci
npm -w @decide/booth run build
rm -rf static/new templates/new/index.html
mv frontend/dist/static/new static
mv frontend/dist/index.html templates/new
