#  Copyright 2022 iFLYTEK. All Rights Reserved.
#  #
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  #
#      http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  ==============================================================================
from iflearner_flow_federate.routes.api import api, sio, socketio_namespace
from iflearner_flow_federate.utils.log import flow_logger

ns = api.namespace("federate", description="Federate API")


@sio.on("register_status", namespace=socketio_namespace)
def register_status(data):
    ret_code = data["ret_code"]
    ret_msg = data["ret_msg"]
    if ret_code == 0:
        flow_logger.info("register success!!!")
    else:
        flow_logger.error(
            f"register fail,  ret_code is:{ret_code}, ret_msg is:{ret_msg}"
        )
