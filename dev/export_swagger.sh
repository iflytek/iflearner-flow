#!/bin/bash
set -e

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../
export PYTHONPATH=$PYTHONPATH:${PWD}/python
export FLOW_SERVER_CONF_PATH=python/iflearner_flow_server/conf/flow_server_dev.yaml
export FLOW_FEDERATE_CONF_PATH=python/iflearner_flow_federate/conf/flow_federate_dev.yaml

# export swagger schema json file to docs
export iflearner_flow_server_swagger_file=${PWD}/doc/docs/api/swagger/iflearner_flow_server_swagger.json
export iflearner_flow_federate_swagger_file=${PWD}/doc/docs/api/swagger/iflearner_flow_federate_swagger.json
python python/iflearner_flow_server/routes/export.py --type 0 --dst_file ${iflearner_flow_server_swagger_file}
python python/iflearner_flow_federate/routes/export.py --type 0 --dst_file ${iflearner_flow_federate_swagger_file}

# export swagger postman json file
export iflearner_flow_server_postman_file=${PWD}/doc/docs/api/postman/iflearner_flow_server_postman.json
export iflearner_flow_federate_postman_file=${PWD}/doc/docs/api/postman/iflearner_flow_federate_postman.json
python python/iflearner_flow_server/routes/export.py --type 1 --dst_file ${iflearner_flow_server_postman_file}
python python/iflearner_flow_federate/routes/export.py --type 1 --dst_file ${iflearner_flow_federate_postman_file}