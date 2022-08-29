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
from flask import request
from flask_restx import Resource, fields
from iflearner_flow_server.routes.api import api, custom_response
from iflearner_flow_server.server.task_manager import TaskManager
from iflearner_flow_server.utils.api_utils import get_json_result
from iflearner_flow_server.utils.log import flow_logger

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
parser.add_argument(
    "federated_id",
    type=str,
    required=False,
    help="The federated id for query",
    location="args",
    default="",
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
        "federate_data": fields.List(
            fields.Nested(federate_data_fields),
            required=True,
            description="The federate data mapping",
        ),
    },
)

party_status = api.model(
    "PartyStatus",
    {
        "name": fields.String(),
        "ready": fields.Boolean(),
        "complete": fields.Boolean(),
        "current_epoch": fields.Integer(),
        "total_epoch": fields.Integer(),
    },
)

task_fields = api.clone(
    "TaskFields",
    task_base_fields,
    {
        "task_id": fields.String(description="The id of task"),
        "status": fields.String(description="The status of task"),
        "party_status": fields.List(
            fields.Nested(party_status), description="The status of parties"
        ),
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

task_create_response = api.model(
    "TaskCreateResponse", {"task_id": fields.String(description="The id of task")}
)

task_start_request = api.model(
    "TaskStartRequest", 
    {
        "epochs": fields.Integer(description="The number of epochs", default=10),
        "hyper_parameter": fields.List(fields.String()),
        "enable_smpc": fields.Boolean(description="Whether to enable smpc.", default=False)
    },
)


def ack():
    flow_logger.debug("message was received!")


@ns.route("")
class TaskList(Resource):
    @ns.expect(task_base_fields)
    @ns.marshal_with(custom_response(task_create_response))
    def post(self):
        """Create a task."""
        flow_logger.debug("receive create task request")
        flow_logger.debug(f"request is:{request.json}")
        task_id = TaskManager().create(
            request.json["name"],
            request.json["template_id"],
            request.json["remark"],
            request.json["federate_data"],
        )
        return get_json_result(data={"task_id": task_id})

    @ns.doc(parser=parser)
    @ns.param("page", "The current page index")
    @ns.param("limit", "The size of current page of query")
    @ns.param("federated_id", "The federated id of query")
    @ns.marshal_with(custom_response(task_list_fields))
    def get(self):
        """List tasks."""
        args = parser.parse_args()
        flow_logger.debug(
            f"task list page is:{args['page']}, limit is:{args['limit']}, federated is is:{args['federated_id']}"
        )
        tasks, count = TaskManager().list(
            "", int(args["page"]), int(args["limit"]), args["federated_id"]
        )
        flow_logger.debug(tasks)
        return get_json_result(data={"tasks": tasks, "task_count": count})


@ns.route("/<string:task_id>")
class Task(Resource):
    @ns.marshal_with(custom_response(task_fields))
    def get(self, task_id: str):
        """Get a specified task."""
        flow_logger.debug(f"receive get a task request, task_id is:{task_id}")
        task = TaskManager().get(task_id)
        flow_logger.info(task)
        return get_json_result(data=task)

    @ns.expect(task_base_fields)
    @ns.marshal_with(custom_response())
    def put(self, task_id: str):
        """Update a specified task."""
        flow_logger.debug(f"receive get a task:{task_id} update request:{request.json}")
        TaskManager().update(
            task_id,
            request.json["name"],  # type: ignore
            request.json["template_id"],  # type: ignore
            request.json["remark"],  # type: ignore
            request.json["federate_data"],  # type: ignore
        )
        return get_json_result()

    @ns.marshal_with(custom_response())
    def delete(self, task_id: str):
        """Delete a specified task."""
        flow_logger.debug(f"receive get a task:{task_id} delete request")
        TaskManager().delete(task_id)
        return get_json_result()


@ns.route("/<string:task_id>/start")
class StartTask(Resource):
    @ns.expect(task_start_request)
    @ns.marshal_with(custom_response())
    def post(self, task_id: str):
        """Start task."""
        flow_logger.debug(f"start task: {task_id}")
        TaskManager().start(task_id, request.json["epochs"], request.json["hyper_parameter"], request.json["enable_smpc"])
        return get_json_result()


@ns.route("/<string:task_id>/stop")
class StopTask(Resource):
    @ns.marshal_with(custom_response())
    def post(self, task_id: str):
        """Stop task."""
        flow_logger.debug(f"stop task: {task_id}")
        TaskManager().stop(task_id)
        return get_json_result()
