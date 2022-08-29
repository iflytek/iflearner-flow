#!/bin/bash
#
#  Copyright 2022 iFLYTEK. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  ==============================================================================
#
set -e
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../../

echo ${PWD}

docker run -itd --name iflearner_flow_federate \
-v ${PWD}/conf/flow_federate_prod.yaml:/data/iflearner_flow/python/iflearner_flow_federate/conf/flow_federate_prod.yaml  \
-v ${PWD}/log:/data/iflearner_flow/python/iflearner_flow_federate/log \
-e FLASK_ENV=production \
-e FLOW_FEDERATE_CONF_PATH="/data/iflearner_flow/python/iflearner_flow_federate/conf/flow_federate_prod.yaml" \
-p 1236:1236 \
iflearner_flow_federate:0.1 python3 app.py