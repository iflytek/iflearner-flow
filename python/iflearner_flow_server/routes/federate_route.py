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
"""The route of federate."""
from typing import Dict, List

from flask import request
from flask_restx import Resource, fields
from flask_socketio import emit, join_room, leave_room
from iflearner_flow_server.routes.api import (
    api,
    custom_response,
    socketio,
    socketio_namespace,
)
from iflearner_flow_server.utils.api_utils import get_json_result
from iflearner_flow_server.utils.base_utils import Singleton
from iflearner_flow_server.utils.log import flow_logger

ns = api.namespace("federate", description="Federate API")


class FederateMeta(object):
    def __init__(self, id: str, name: str, host: str):
        self.id = id
        self.name = name
        self.host = host

    def __repr__(self) -> str:
        return f"`id:{self.id} name:{self.name} host:{self.host}`"

    def __str__(self) -> str:
        return f"`id:{self.id} name:{self.name} host:{self.host}`"


@Singleton
class FederateMemberManager(object):
    def __init__(self):
        self._members: Dict[str, FederateMeta] = {}

    def add(self, sid: str, member: FederateMeta):
        self._members[sid] = member

    def delete(self, sid: str):
        if sid in self._members:
            self._members.pop(sid)

    def get(self, sid: str) -> FederateMeta:
        return self._members[sid]

    def valid_sid(self, sid) -> bool:
        return True if sid in self._members else False

    def members(self) -> List[FederateMeta]:
        members: List[FederateMeta] = []
        for member in self._members.values():
            members.append(member)
        return members

    def valid_member(self, check_member: FederateMeta) -> bool:
        for member in self._members.values():
            if member.id == check_member.id and member.name == check_member.name:
                return True
        return False


federate_member_manager = FederateMemberManager()


@socketio.on_error(namespace=socketio_namespace)
def error_handler(e):
    flow_logger.error(f"socketio receive error:{e}")


@socketio.on("disconnect", namespace=socketio_namespace)
def disconnect():
    sid = request.sid
    flow_logger.debug(f"sid:{sid} disconnected")
    if federate_member_manager.valid_sid(sid):
        federate_meta = federate_member_manager.get(sid)
        leave_room(federate_meta)
        federate_member_manager.delete(sid)
        flow_logger.debug(f"sid:{sid} federate:{federate_meta} leave room")


@socketio.on("connect", namespace=socketio_namespace)
def connect():
    flow_logger.debug(f"sid:{request.sid} connected")


def valid_federate_meta(federate_meta: FederateMeta) -> bool:
    for registered_federate in federate_member_manager.members():
        if (registered_federate.id == federate_meta.id) or (
            registered_federate.name == federate_meta.name
        ):
            return False
    return True


def get_federate_members() -> List[Dict[str, str]]:
    members = []
    for registered_federate in federate_member_manager.members():
        members.append({"id": registered_federate.id, "name": registered_federate.name})
    return members


def ack():
    flow_logger.debug("message was received!")


@socketio.on("register", namespace=socketio_namespace)
def register(message):
    sid = request.sid
    flow_logger.debug(f"sid:{sid} will register")
    federate_id = message["id"]
    federate_name = message["name"]
    host = message["host"]
    federate_meta = FederateMeta(id=federate_id, name=federate_name, host=host)
    if not valid_federate_meta(federate_meta):
        emit(
            "register_status",
            {"ret_code": 1, "ret_msg": "federate id or name has been registered!"},
        )
        flow_logger.error(
            f"sid:{sid} federate:{federate_meta} id or name has been registed!"
        )
        return
    join_room(federate_meta)
    federate_member_manager.add(sid, federate_meta)
    socketio.emit(
        "register_status",
        {"ret_code": 0, "ret_msg": "success"},
        callback=ack,
        namespace=socketio_namespace,
    )
    flow_logger.debug(f"sid:{sid} federate:{federate_meta} register success!")


@socketio.on("unregister", namespace=socketio_namespace)
def unregister():
    sid = request.sid
    flow_logger.debug(f"sid:{sid} will unregister")
    if federate_member_manager.valid_sid(sid):
        federate_meta = federate_member_manager
        leave_room(federate_meta)
        emit(
            "unregister_status",
            {"ret_code": 0, "ret_msg": "success"},
            namespace=socketio_namespace,
        )
        flow_logger.debug(f"sid:{sid} federate:{federate_meta} unregister success!")
    else:
        emit("unregister_status", {"ret_code": 2, "ret_msg": "federate not registered"})
        flow_logger.debug(f"sid:{sid} not registered")


federate_fields = api.model(
    "FederateField",
    {
        "name": fields.String(description="The name of federate"),
        "id": fields.String(description="The id of federate"),
    },
)

federate_list_fields = api.model(
    "FederateList",
    {
        "federates": fields.List(fields.Nested(federate_fields)),
        "federate_count": fields.Integer(
            description="sum of federate members for query"
        ),
    },
)


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


@ns.route("")
class FederateList(Resource):
    @ns.doc(parser=parser)
    @ns.param("page", "The current page index")
    @ns.param("limit", "The size of current page of query")
    @ns.marshal_with(custom_response(federate_list_fields))
    def get(self):
        """List Federated members."""
        args = parser.parse_args()
        flow_logger.debug(
            f"federate list page is:{args['page']}, limit is:{args['limit']}"
        )
        return get_json_result(
            data={
                "federates": get_federate_members(),
                "federate_count": len(get_federate_members()),
            }
        )
