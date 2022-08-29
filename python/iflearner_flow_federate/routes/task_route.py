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
"""The route of task."""
from flask_restx import Resource, fields
from iflearner_flow_federate.routes.api import (
    api,
    custom_response,
    sio,
    socketio_namespace,
)
from iflearner_flow_federate.server.task_manager import TaskManager
from iflearner_flow_federate.utils.api_utils import get_json_result
from iflearner_flow_federate.utils.log import flow_logger

ns = api.namespace("task", description="Task API")

parser = api.parser()
parser.add_argument(
    "page",
    type=int,
    required=False,
    help="The current page index",
    location="args",
    default=1,
)
parser.add_argument(
    "limit",
    type=int,
    required=False,
    help="The size of current page for query",
    location="args",
    default=10,
)

federate_data_fields = api.model(
    "FederateDataFields",
    {
        "federated_id": fields.String(
            required=True, description="The id of federate member"
        ),
        "federated_data": fields.String(
            required=True, description="The data path of federate"
        ),
    },
)

task_base_fields = api.model(
    "TaskBaseFields",
    {
        "name": fields.String(
            required=True, description="The name of task", min_length=3, max_length=50
        ),
        "remark": fields.String(
            required=False, description="The name of task", min_length=0, max_length=500
        ),
        "template_id": fields.String(required=True, description="The id of template"),
        "federate_datas": fields.List(
            fields.Nested(federate_data_fields),
            required=True,
            description="The federate data mapping",
        ),
    },
)

task_fields = api.clone(
    "TaskFields",
    task_base_fields,
    {
        "task_id": fields.String(description="The id of task"),
        "status": fields.String(description="The status of task"),
        "create_time": fields.DateTime(
            dt_format="rfc822", description="The create time of task"
        ),
        "modify_time": fields.DateTime(
            dt_format="rfc822", description="The update time of task"
        ),
    },
)

task_list_fields = api.model(
    "TaskList",
    {
        "tasks": fields.List(fields.Nested(task_fields)),
        "task_count": fields.Integer(description="sum of query"),
    },
)

logs_fields = api.model("LogsFields", {"logs": fields.List(fields.String())})


@ns.route("")
class TaskList(Resource):
    @ns.doc(parser=parser)
    @ns.param("page", "The current page index")
    @ns.param("limit", "The size of current page of query")
    @ns.marshal_with(custom_response(task_list_fields))
    def get(self):
        """List tasks."""

        args = parser.parse_args()
        flow_logger.debug(f"task list page is:{args['page']}, limit is:{args['limit']}")
        data = TaskManager().list("", int(args["page"]), int(args["limit"]))
        flow_logger.debug(data)
        return get_json_result(data=data)


@ns.route("/<string:task_id>")
class Task(Resource):
    @ns.marshal_with(custom_response(task_fields))
    def get(self):
        pass


@ns.route("/<string:task_id>/logs")
class TaskLogs(Resource):
    @ns.marshal_with(custom_response(logs_fields))
    def get(self, task_id: str):
        """Get the task logs."""
        flow_logger.debug(f"get task logs: {task_id}")
        logs = TaskManager().logs(task_id)
        return get_json_result(data={"logs": logs})


@sio.on("start_task", namespace=socketio_namespace)
def start_task(data):
    """data can be a dict."""
    flow_logger.debug(f"receive start task message:{data} from server.")
    TaskManager().start(data["task_id"], data["epochs"], data["hyper_parameter"], data["other_parties"])


@sio.on("stop_task", namespace=socketio_namespace)
def stop_task(data):
    """data can be a dict."""
    flow_logger.debug(f"receive stop task message:{data} from server.")
    TaskManager().stop(data["task_id"])
