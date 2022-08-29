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
"""Task manager, include start, stop, status, etc..."""
import typing
import uuid
from typing import List

from iflearner_flow_server.errors import error
from iflearner_flow_server.models.models import Task, TaskParty, db
from iflearner_flow_server.routes.api import socketio, socketio_namespace
from iflearner_flow_server.routes.federate_route import federate_member_manager
from iflearner_flow_server.utils.conf import conf_inst
from iflearner_flow_server.utils.log import flow_logger
from iflearner_job import iflearner_job


def ack():
    flow_logger.debug("message was received!")


class TaskManager(object):
    @classmethod
    def create(
        cls,
        name: str,
        template_id: str,
        remark: str,
        federate_data: List,
    ) -> str:
        """Create a task by specified template.

        Args:
            name: The name of task, and it should be unique.
            template_id (str): The id of template.
            remark: Remark information
            federate_data (Dict(str, List[str])): The mapping data of federate members.

        Returns:
            (str): The id of generated task.
        """

        if name == "":
            raise error.TaskError().TaskNameEmpty

        existed = Task.query.filter_by(name=name).first()
        if existed is not None:
            raise error.TaskError().TaskNameDuplicate

        task_id = uuid.uuid4().hex
        task = Task(task_id=task_id, template_id=template_id, name=name, remark=remark)
        for data in federate_data:
            task.parties.append(
                TaskParty(
                    task_id=task_id,
                    party_name=data["federated_id"],
                    volumes=data["federated_data"],
                )
            )

        db.session.add(task)
        db.session.commit()

        return task_id

    @classmethod
    def update(
        cls,
        task_id: str,
        name: str,
        template_id: str,
        remark: str,
        federate_data: List,
    ):
        """Update a specified task.

        Args:
            task_id (str): The id of task.
            name: The name of task, and it should be unique.
            template_id (str): The id of template.
            remark: remark information
            federate_data: (Dict(str, List[str])): The mapping data of federate members.

        Returns:
        """

        task = cls._get(task_id)
        task.name = name
        task.template_id = template_id
        task.remark = remark
        task.parties = []
        for data in federate_data:
            task.parties.append(
                TaskParty(
                    task_id=task_id,
                    party_name=data["federated_id"],
                    volumes=data["federated_data"],
                )
            )

        db.session.commit()

    @classmethod
    def start(
        cls, 
        task_id: str, 
        epochs: int=10, 
        hyper_parameter: list=None,
        enable_smpc: bool=False,
    ):
        """Start the specified task.

        Args:
            task_id (str): The id of task.
            epochs (int): The number of epochs.
            hyper_parameter (list): The hyper_parameter of template.
            enable_smpc (bool): Enable smpc.

        Returns:
        """

        task = cls._get(task_id)
        if iflearner_job.is_active(task.status):
            raise error.TaskError().TaskStatusConflicit

        if task.status != None and task.status != "":
            cls._stop_task(task)

        args = conf_inst.flow_conf.iflearner_server_args
        args.append("-n=" + str(len(task.parties)))
        args.append(f"--epochs={epochs}")

        for party in task.parties:
            members = federate_member_manager.members()
            other_parties = []
            dst = None
            for item in members:
                if party.party_name == item.id:
                    dst = item
                else:
                    other_parties.append(item.host)

            if dst is None:
                raise error.TaskError().TaskPartyNotFound
            else:
                if not enable_smpc:
                    other_parties = []
                socketio.emit(
                    "start_task",
                    {"task_id": task_id, "epochs": epochs, "hyper_parameter": hyper_parameter, "other_parties": other_parties},
                    namespace=socketio_namespace,
                    to=dst,
                    callback=ack,
                )

        ifl_job = iflearner_job.IflearnerJob(task_id, iflearner_job.RoleServer)
        ifl_job.create(conf_inst.flow_conf.iflearner_server_image, None, args)

        task.status = iflearner_job.IflearnerJobStarted
        db.session.commit()

    @classmethod
    def get(cls, task_id: str, party_name: str = None):
        """Get specified task.

        Args:
            task_id (str): The id of task.
            party_name (str): use party name to get specified party configuration, and if party name is empty, it means to get whole task information.

        Returns:
        """

        task = cls._get(task_id)
        task_dict = task.as_dict()
        task_dict["federate_data"] = [party.as_dict() for party in task.parties]
        try:
            party_status = iflearner_job.IflearnerJob(
                task.task_id, iflearner_job.RoleServer
            ).client_status()
            task_dict["party_status"] = party_status
        except iflearner_job.IflearnerJobException as e:
            flow_logger.error(e)
        return task_dict

    @classmethod
    def _get(cls, task_id: str) -> Task:
        task = Task.query.filter_by(task_id=task_id).first()
        if task is None:
            raise error.TaskError().TaskNotFound

        if iflearner_job.is_active(task.status):
            try:
                ifl_job = iflearner_job.IflearnerJob(task.task_id, iflearner_job.RoleServer)
                task.status = ifl_job.status()
            except iflearner_job.IflearnerJobException as e:
                flow_logger.error(e)
                if e.reason == "Not Found":
                    task.status = ""
            
            db.session.commit()

        return task

    @classmethod
    def list(
        cls, keyword: str, page: int = 1, limit: int = 10, federated_id: str = ""
    ) -> typing.Tuple[list, int]:
        """List task.

        Args:
            keyword (str): Keywords for fuzzy query.
            page (int): Current page number for query.
            limit (int): Limit Size for current page query.

        Returns:
            (list): The list of task.
        """

        if federated_id != "":
            tasks = (
                Task.query.join(TaskParty)
                .filter(TaskParty.party_name == federated_id)
                .offset((page - 1) * limit)
                .limit(limit)
                .all()
            )
            count = (
                Task.query.join(TaskParty)
                .filter(TaskParty.party_name == federated_id)
                .count()
            )
        else:
            tasks = Task.query.offset((page - 1) * limit).limit(limit).all()
            count = Task.query.count()

        task_list = []
        for task in tasks:
            task_list.append(cls.get(task.task_id))

        return task_list, count

    @classmethod
    def stop(cls, task_id: str):
        """Stop the specified task.

        Args:
            task_id (str): The id of task.

        Returns:
        """

        task = cls._get(task_id)
        if not iflearner_job.is_active(task.status):
            raise error.TaskError().TaskStatusConflicit

        cls._stop_task(task)

        task.status = iflearner_job.IflearnerJobCancelled
        db.session.commit()

    @classmethod
    def delete(cls, task_id: str):
        """Delete the specified job.

        Args:
            task_id (str): The id of task.

        Returns:
        """

        task = cls._get(task_id)
        if iflearner_job.is_active(task.status):
            raise error.TaskError().TaskStatusConflicit

        cls._stop_task(task)

        for party in task.parties:
            db.session.delete(party)
        db.session.delete(task)
        db.session.commit()

    @classmethod
    def _stop_task(cls, task: Task) -> None:
        flow_logger.info(
            f"delete IflearnerJob, task id: {task.task_id}, task status: {task.status}"
        )
        if (
            task.status is not None
            and task.status != iflearner_job.IflearnerJobCancelled
        ):
            for party in task.parties:
                members = federate_member_manager.members()
                existed = False
                for item in members:
                    if party.party_name == item.id:
                        existed = True
                        socketio.emit(
                            "stop_task",
                            {"task_id": task.task_id},
                            namespace=socketio_namespace,
                            to=item,
                            callback=ack,
                        )
                        break

                if not existed:
                    raise error.TaskError().TaskPartyNotFound

            ifl_job = iflearner_job.IflearnerJob(task.task_id, iflearner_job.RoleServer)
            ifl_job.delete()
