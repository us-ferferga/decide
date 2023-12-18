#!/bin/bash

set -e

## If the command has not been replaced by the user (i.e docker run image /bin/bash),
## follow through the setup process
if [[ "$*" = "/scripts/run.sh" ]]; then
    echo "==== Starting Decide setup ===="
    echo
    /scripts/setup.sh
    echo
    echo "====      Setup finished!        ===="
    echo -e "\n"
fi

exec "$@"
