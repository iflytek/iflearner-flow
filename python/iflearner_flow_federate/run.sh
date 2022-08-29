#!/bin/bash
set -e

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../

export PYTHONPATH=${PWD}:$PYTHONPATH
echo $PYTHONPATH

cd iflearner_flow_federate

export FLASK_APP=app.py
#export FLASK_ENV=development
export FLOW_FEDERATE_CONF_PATH="conf/flow_federate_dev.yaml"
export FLASK_ENV=production
flask run --host 0.0.0.0 --port 1236