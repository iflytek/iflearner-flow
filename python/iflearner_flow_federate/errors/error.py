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
from iflearner_flow_federate.errors import IflearnerFlowFederateError


class Success(object):
    SuccessResponse = IflearnerFlowFederateError()


class TaskError(object):
    TaskIflearnerFlowServerInternalError = IflearnerFlowFederateError(
        ret_code=20100, ret_msg="call iflearner_flow_server internal error"
    )
    TaskIflearnerFlowServerRetCodeError = IflearnerFlowFederateError(
        ret_code=20101, ret_msg="call iflearner_flow_server ret code error"
    )
