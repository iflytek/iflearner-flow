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

from typing import Any, Dict, List

from flow_server_sdk.api import flow_server_api_base
from flow_server_sdk.utils.http_utils import delete, get, post, put

class TaskManager(object):
    task_route = "/api/v1/task"

    # @staticmethod
    # @property
    def base_url():
        return flow_server_api_base.generate_base_url(TaskManager.task_route)

    @classmethod
    def create(
        cls,
        name: str,
        template_id: str,
        remark: str,
        federate_data: List[Any],
    ) -> Dict[str, Any]:
        """Create a task by specified template.

        Args:
            name: The name of task, and it should be unique.
            template_id (str): The id of template.
            remark: Remark information
            federate_data (Dict(str, List[str])): The mapping data of federate members.

        Returns:
            Returns (Dict[str, Any]): The response in json format
        """

        data = {
            "name": name,
            "template_id": template_id,
            "remark": remark,
            "federate_data": federate_data,
        }

        return post(url=cls.base_url(), data=data)

    @classmethod
    def update(cls,
        task_id: str,
        name: str,
        template_id: str,
        remark: str,
        federate_data: List,
    ) -> Dict[str, Any]:
        """Update a specified task.

        Args:
            task_id (str): The id of task.
            name: The name of task, and it should be unique.
            template_id (str): The id of template.
            remark: remark information
            federate_data: (Dict(str, List[str])): The mapping data of federate members.

        Returns:
            Returns (Dict[str, Any]): The response in json format
        """

        data = {
            "name": name,
            "template_id": template_id,
            "remark": remark,
            "federate_data": federate_data,
        }
        return put(url=f"{cls.base_url()}/{task_id}", data=data)

    @classmethod
    def get(cls, task_id: str) -> Dict[str, Any]:
        """Get specified task.

        Args:
            task_id (str): The id of task.

        Returns:
            Returns (Dict[str, Any]): The response in json format
        """

        return get(f"{cls.base_url()}/{task_id}")

    @classmethod
    def list(cls, page: int, limit: int) -> Dict[str, Any]:
        """List task.

        Args:
            page (int): Current page number for query.
            limit (int): Limit Size for current page query.

        Returns:
            Returns (Dict[str, Any]): The response in json format
        """

        return get(f"{cls.base_url()}?page={page}&limit={limit}")

    @classmethod
    def delete(cls, task_id: str) -> Dict[str, Any]:
        """Delete the specified job.

        Args:
            task_id (str): The id of task.

        Returns:
            Returns (Dict[str, Any]): The response in json format
        """

        return delete(f"{cls.base_url()}/{task_id}")

    @classmethod
    def start(cls, task_id: str) -> Dict[str, Any]:
        """Start the specified task.

        Args:
            task_id (str): The id of task.

        Returns:
            Returns (Dict[str, Any]): The response in json format
        """

        return post(url=f"{cls.base_url()}/{task_id}/start")

    @classmethod
    def stop(cls, task_id: str) -> Dict[str, Any]:
        """Stop the specified task.

        Args:
            task_id (str): The id of task.

        Returns:
            Returns (Dict[str, Any]): The response in json format
        """

        return post(url=f"{cls.base_url()}/{task_id}/stop")
