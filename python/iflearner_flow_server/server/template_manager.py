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
"""Template manager, include create, query, delete, etc..."""
import json
import uuid
from typing import Any, List, Tuple

from iflearner_flow_server.errors.error import CommonError, TemplateError
from iflearner_flow_server.models.models import Template, db


class TemplateManager(object):
    @classmethod
    def valid_template_create_request(cls, name: str, image_url: str):
        if len(name) < 3 or len(name) > 50:
            raise CommonError.RequestParamResonse.set_ret_msg(
                "Please set the name parameter length between 3 and 50"
            )
        if image_url == "" or len(image_url) > 255:
            raise CommonError.RequestParamResonse.set_ret_msg(
                "Please set the image_url parameter length between 1 and 255"
            )

    @classmethod
    def create(
        cls,
        name: str,
        image_url: str,
        workdir: str,
        command: List[str],
        remark: str = None,
        hyper_parameter: list = None,
    ) -> str:
        """Create a template for task.

        Args:
            name (str): The name of template.
            image_url (str): The image url of template.
            workdir (str): The workdir of container.
            command (List[str]): The start command of container.
            remark (str): The remark of template.
            hyper_parameter (list): The hyper_parameter of template.

        Returns:
        """
        cls.valid_template_create_request(name=name, image_url=image_url)

        query_template = Template.query.filter_by(name=name).first()
        if query_template is not None:
            raise TemplateError.TemplateRepeat

        template_id = uuid.uuid4().hex[:30]
        template = Template(
            id=template_id,
            name=name,
            remark=remark,
            image_url=image_url,
            workdir=workdir,
            command=json.dumps(command),
            hyper_parameter=json.dumps(hyper_parameter),
        )
        db.session.add(template)
        db.session.commit()
        return template_id

    @classmethod
    def get(cls, template_id: str):
        """Get specified template.

        Args:
            template_id (str): The id of template.

        Returns:
        """
        template = Template.query.filter_by(id=template_id).first()
        if template is None:
            raise TemplateError.TemplateNotFound
        template_dict = template.as_dict()
        template_dict["hyper_parameter"] = json.loads(template_dict["hyper_parameter"])
        template_dict["template_id"] = template_dict["id"]
        template_dict["command"] = json.loads(template_dict["command"])
        return template_dict

    @classmethod
    def list(
        cls, keyword: str, page: int = 1, limit: int = 10
    ) -> Tuple[List[dict], int]:
        """List template.

        Args:
            keyword (str): Keywords for fuzzy query.
            page (int): Current page number for query.
            limit (int): Limit Size for current page query.

        Returns:
            (list): The list of template.
        """

        templates = Template.query.offset((page - 1) * limit).limit(limit).all()
        count = Template.query.count()

        template_list = []
        for template in templates:
            template_dict = template.as_dict()
            template_dict["hyper_parameter"] = json.loads(
                template_dict["hyper_parameter"]
            )
            template_dict["template_id"] = template_dict["id"]
            template_dict["command"] = json.loads(template_dict["command"])
            template_list.append(template_dict)
        return template_list, count

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
    ):
        """Delete the specified template.

        Args:
            template_id (str): The id of template.
            name (str): The name of template.
            image_url (str): The image url of template.
            workdir (str): The workdir of container.
            command (List[str]): The start command of container.
            remark (str): The remark of template.
            hyper_parameter (List[Any]): The hyper_parameter of template.

        Returns:
        """
        template = Template.query.filter_by(id=template_id).first()
        if template is None:
            raise TemplateError.TemplateNotFound
        if name != template.name:
            template1 = Template.query.filter_by(name=name).first()
            if template1 is not None:
                raise TemplateError.TemplateRepeat
        cls.valid_template_create_request(name=name, image_url=image_url)
        template.name = name
        template.image_url = image_url
        template.workdir = workdir
        template.command = json.dumps(command)
        template.remark = remark
        template.hyper_parameter = json.dumps(hyper_parameter)
        db.session.commit()
        return

    @classmethod
    def delete(cls, template_id: str):
        """Delete the specified template.

        Args:
            template_id (str): The id of template.

        Returns:
        """
        template = Template.query.filter_by(id=template_id).first()
        if template is None:
            raise TemplateError.TemplateNotFound
        db.session.delete(template)
        db.session.commit()
        return
