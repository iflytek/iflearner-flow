#!/bin/bash
set -e

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../
export PYTHONPATH=${PWD}:$PYTHONPATH
echo $PYTHONPATH

cd iflearner_flow_server

export FLASK_ENV=development
export FLOW_SERVER_CONF_PATH="conf/flow_server_dev.yaml"
python3 app.py