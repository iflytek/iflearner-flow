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


class TemplateManager(object):
    template_uri = "/api/v1/template"

    @classmethod
    @property
    def base_url(cls):
        return flow_server_api_base.generate_base_url(TemplateManager.template_uri)

    @classmethod
    def create(
        cls,
        name: str,
        image_url: str,
        workdir: str,
        command: List[str],
        remark: str = None,
        hyper_parameter: list = None,
    ) -> Dict[str, Any]:
        """Create a template for task.

        Args:
            name (str): The name of template.
            image_url (str): The image url of template.
            workdir (str): The workdir of container.
            command (List[str]): The start command of container.
            remark (str): The remark of template.
            hyper_parameter (list): The hyper_parameter of template.

        Returns (Dict[str, Any]): The response in json format
        """
        data = {
            "name": name,
            "image_url": image_url,
            "workdir": workdir,
            "command": command,
            "remark": remark,
            "hyper_parameter": hyper_parameter,
        }
        return post(url=cls.base_url, data=data)

    @classmethod
    def update(
        cls,
        template_id: str,
        name: str,
        image_url: str,
        workdir: str,
        command: List[str] = [],
        remark: str = "",
        hyper_parameter: List[Any] = [],
    ) -> Dict[str, Any]:
        """Update a template.

        Args:
            template_id (str): The id of template.
            name (str): The name of template.
            image_url (str): The image url of template.
            workdir (str): The workdir of container.
            command (List[str]): The start command of container.
            remark (str): The remark of template.
            hyper_parameter (list): The hyper_parameter of template.

        Returns (Dict[str, Any]): The response in json format
        """
        data = {
            "name": name,
            "image_url": image_url,
            "workdir": workdir,
            "command": command,
            "remark": remark,
            "hyper_parameter": hyper_parameter,
        }
        return put(url=f"{cls.base_url}/{template_id}", data=data)

    @classmethod
    def get(cls, template_id: str) -> Dict[str, Any]:
        """Get specified template.

        Args:
            template_id (str): The id of template.

        Returns (Dict[str, Any]): The response in json format
        """
        return get(f"{cls.base_url}/{template_id}")

    @classmethod
    def list(cls, keyword: str = "", page: int = 1, limit: int = 10) -> Dict[str, Any]:
        """List Template by specified query param.

        Args:
            keyword (str): Keywords for fuzzy query.
            page (int): Current page number for query.
            limit (int): Limit Size for current page query.

        Returns (Dict[str, Any]): The response in json format
        """
        return get(
            url=cls.base_url, param={"keyword": keyword, "page": page, "limit": limit}
        )

    @classmethod
    def delete(cls, template_id: str) -> Dict[str, Any]:
        """Delete specified template.

        Args:
            template_id (str): The id of template.

        Returns (Dict[str, Any]): The response in json format
        """
        return delete(url=f"{cls.base_url}/{template_id}")
