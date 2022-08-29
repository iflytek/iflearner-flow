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
import uuid
from typing import Any

from flask import Blueprint, Flask
from flask_restx import Api, fields
from flask_socketio import SocketIO
from iflearner_flow_server.utils.log import socketio_logger

app = Flask(__name__)
app.config.SWAGGER_UI_OPERATION_ID = True  # type: ignore
app.config.SWAGGER_UI_REQUEST_DURATION = True  # type: ignore
app.url_map.strict_slashes = False
app.config["JSON_AS_ASCII"] = False
app.config["ERROR_INCLUDE_MESSAGE"] = False  # 必须设置为False
app.config["SECRET_KEY"] = "secret!"
# app.config["SERVER_NAME"] = "127.0.0.1"
# app.app_context().__enter__()

# # disable Try it Out for all methods
# app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = []
# # enable Try it Out for specific methods
# app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post"]
socketio = SocketIO(
    app,
    logger=socketio_logger,
    engineio_logger=socketio_logger,
    cors_allowed_origins="*",
    async_mode="eventlet",
)  # need `pip install eventlet`
socketio_namespace = "/iflearner-flow"

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    version="1.0",
    title="Iflearner Flow Server API",
    description="Iflearner Flow Server API",
    doc="/doc",
)


def custom_response(data: Any = None) -> Any:
    if data is not None:
        custom_model = api.model(
            "CustomResponse" + str(uuid.uuid4()),
            {
                "ret_code": fields.Integer(description="The code of result", default=0),
                "ret_msg": fields.String(
                    description="The message of result", default="success"
                ),
                "data": fields.Nested(data),
            },
        )
    else:
        custom_model = api.model(
            "CustomResponse",
            {
                "ret_code": fields.Integer(description="The code of result", default=0),
                "ret_msg": fields.String(
                    description="The message of result", default="success"
                ),
            },
        )
    return custom_model
