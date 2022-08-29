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
from iflearner_flow_server.errors import IflearnerFlowServerError


class Success(object):
    SuccessResponse = IflearnerFlowServerError()


class CommonError(object):
    RequestParamResonse = IflearnerFlowServerError(
        ret_code=10000, ret_msg="request param invalid"
    )


class FederateError(object):
    FederateRepeatRegister = IflearnerFlowServerError(
        ret_code=10100, ret_msg="federate has been registered"
    )


class TemplateError(object):
    TemplateNotFound = IflearnerFlowServerError(
        ret_code=10200, ret_msg="template not found"
    )
    TemplateRepeat = IflearnerFlowServerError(
        ret_code=10201, ret_msg="duplicate template name"
    )
    TemplateNameEmpty = IflearnerFlowServerError(
        ret_code=10202, ret_msg="empty template name"
    )


class TaskError(object):
    TaskNotFound = IflearnerFlowServerError(ret_code=10300, ret_msg="task not found")
    TaskNameDuplicate = IflearnerFlowServerError(
        ret_code=10301, ret_msg="duplicate task name"
    )
    TaskNameEmpty = IflearnerFlowServerError(ret_code=10302, ret_msg="empty task name")
    TaskStatusConflicit = IflearnerFlowServerError(
        ret_code=10303, ret_msg="status conflicit"
    )
    TaskPartyNotFound = IflearnerFlowServerError(
        ret_code=10304, ret_msg="task party not found"
    )
