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
"""The Api util."""
from iflearner_flow_server.errors import IflearnerFlowServerError
from iflearner_flow_server.errors.error import Success
from iflearner_flow_server.routes.api import api


def get_json_result(
    custom_err: IflearnerFlowServerError = Success.SuccessResponse, data=None
):
    """Get API json result.

    Args:
        custom_err (IflearnerFlowServerError): The Error class include ret_msg and ret_code.
        data (Any): The custom result data.

    Returns:
    """
    result_dict = {"ret_code": custom_err.ret_code(), "ret_msg": custom_err.ret_msg()}
    if data is not None:
        result_dict["data"] = data
    return result_dict


@api.errorhandler(IflearnerFlowServerError)
def iflearner_flow_server_error(e):
    return get_json_result(e), 200


@api.errorhandler(Exception)
def server_internal_err_response(e):
    return "internal server error", 500
