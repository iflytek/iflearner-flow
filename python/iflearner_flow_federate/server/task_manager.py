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
"""The task manager."""

import json
import logging
import typing

import requests
from iflearner_flow_federate.errors.error import TaskError
from iflearner_flow_federate.utils.conf import conf_inst
from iflearner_job import iflearner_job
from iflearner_flow_federate.utils.log import flow_logger


class TaskManager(object):
    task_url = "/task/"
    template_url = "/template/"

    @classmethod
    def _http_get(cls, url):
        resp = requests.get(url)
        if resp.status_code != 200:
            raise TaskError().TaskIflearnerFlowServerInternalError

        content = json.loads(resp.content)
        if content["ret_code"] != 0:
            raise TaskError().TaskIflearnerFlowServerRetCodeError

        return content["data"]

    @classmethod
    def start(
        cls, 
        task_id: str,
        epochs: int=10, 
        hyper_parameter: list=None,
        other_parties: typing.List[str] = None,
    ):
        """Process task start when receive start commannd from server.

        Args:
            task_id (str): The id of task.
            epochs (int): The number of epochs.
            hyper_parameter (list): The hyper_parameter of template.
            other_parties: When using SMPC, you need to specify the addresses of other parties.

        Returns:
        """

        flow_logger.info(f"start task: {task_id}")
        task = cls._http_get(
            conf_inst.flow_conf.federate_server_http_uri + cls.task_url + task_id
        )
        volume = None
        for party in task["federate_data"]:
            if conf_inst.flow_conf.federate_id == party["federated_id"]:
                volume = party["federated_data"]

        template = cls._http_get(
            conf_inst.flow_conf.federate_server_http_uri
            + cls.template_url
            + task["template_id"]
        )

        ifl_job = iflearner_job.IflearnerJob(
            task_id + "-" + conf_inst.flow_conf.federate_id, iflearner_job.RoleClient
        )
        command = template["command"]
        command.append("--name=" + conf_inst.flow_conf.federate_id)
        command.append(f"--epochs={epochs}")
        ifl_job.create(template["image_url"], template["workdir"], command, task_id, volume, other_parties)

    @classmethod
    def stop(cls, task_id: str):
        """Process task stop when receive stop commannd from server.

        Args:
            task_id (str): The id of task

        Returns:
        """

        ifl_job = iflearner_job.IflearnerJob(
            task_id + "-" + conf_inst.flow_conf.federate_id, iflearner_job.RoleClient
        )
        ifl_job.delete()

    @classmethod
    def list(cls, keyword: str, page: int = 1, limit: int = 10) -> list:
        """List task.

        Args:
            keyword (str): Keywords for fuzzy query.
            page (int): Current page number for query.
            limit (int): Limit Size for current page query.

        Returns:
            (list): The list of task.
        """

        resp = requests.get(
            conf_inst.flow_conf.federate_server_http_uri
            + cls.task_url
            + "?page={}&limit={}&federated_id={}".format(
                page, limit, conf_inst.flow_conf.federate_id
            )
        )
        logging.debug(resp.content)
        if resp.status_code != 200:
            raise TaskError().TaskIflearnerFlowServerInternalError

        content = json.loads(resp.content)
        return content["data"]

    @classmethod
    def get(cls, task_id: str):
        """Get task information.

        Args:
            task_id (str): The id of task.

        Returns:
        """

        ifl_job = iflearner_job.IflearnerJob(
            task_id + "-" + conf_inst.flow_conf.federate_id, iflearner_job.RoleClient
        )
        ifl_job.status()

    @classmethod
    def logs(cls, task_id: str) -> typing.List[str]:
        """Get task logs.

        Args:
            task_id (str): The id of task.

        Returns:
        """

        ifl_job = iflearner_job.IflearnerJob(
            task_id + "-" + conf_inst.flow_conf.federate_id, iflearner_job.RoleClient
        )
        return ifl_job.logs().split("\n")
