#!/bin/bash

set -e

pushd "decide/booth" > /dev/null
./deploy_frontend.sh
popd > /dev/null

rm -rf $(find . -name node_modules)
