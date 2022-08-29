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
"""The route of template."""
from flask import request
from flask_restx import Resource, fields
from iflearner_flow_server.routes.api import api, custom_response
from iflearner_flow_server.server.template_manager import TemplateManager
from iflearner_flow_server.utils.api_utils import get_json_result
from iflearner_flow_server.utils.log import flow_logger

ns = api.namespace("template", description="Template  API")

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


template_base_fields = api.model(
    "TemplateBaseFields",
    {
        "name": fields.String(required=True, description="The name of template"),
        "remark": fields.String(required=True, description="The name of template"),
        "image_url": fields.String(required=True, description="The url of image"),
        "workdir": fields.String(required=True, description="The workdir of container"),
        "command": fields.List(
            fields.String, required=False, description="The start command of container"
        ),
        "hyper_parameter": fields.List(
            fields.String, required=False, description="The hyper paramter for train"
        ),
    },
)

template_fields = api.clone(
    "TemplateFields",
    template_base_fields,
    {
        "template_id": fields.String(description="The id of template"),
        "create_time": fields.DateTime(
            dt_format="rfc822", description="The create time of template"
        ),
        "modify_time": fields.DateTime(
            dt_format="rfc822", description="The modify time of template"
        ),
    },
)

template_list_fields = api.model(
    "TemplateList",
    {
        "templates": fields.List(fields.Nested(template_fields)),
        "template_count": fields.Integer(description="sum of query"),
    },
)

template_create_response = api.model(
    "TemplateCreateResponse",
    {"template_id": fields.String(description="The id of template")},
)


@ns.route("")
class TemplateList(Resource):
    @ns.expect(template_base_fields)
    @ns.marshal_with(custom_response(template_create_response))
    def post(self):
        """Create a template."""
        flow_logger.debug(f"receive create template request:{request.json}")
        template_id = TemplateManager.create(
            name=request.json.get("name", ""),
            image_url=request.json.get("image_url", ""),
            remark=request.json.get("remark", ""),
            workdir=request.json.get("workdir", ""),
            command=request.json.get("command", []),
            hyper_parameter=request.json.get("hyper_parameter", []),
        )
        return get_json_result(data={"template_id": template_id})

    @ns.doc(parser=parser)
    @ns.param("page", "The current page index")
    @ns.param("limit", "The size of current page of query")
    @ns.marshal_with(custom_response(template_list_fields))
    def get(self):
        """List templates."""
        args = parser.parse_args()
        flow_logger.debug(
            f"template list page is:{args['page']}, limit is:{args['limit']}"
        )
        templates, count = TemplateManager.list(
            keyword="", page=args.get("page", 1), limit=args.get("limit", 10)
        )
        return get_json_result(data={"templates": templates, "template_count": count})


@ns.route("/<string:template_id>")
class Template(Resource):
    @ns.marshal_list_with(custom_response(template_fields))
    def get(self, template_id: str):
        """Get a specified template."""
        flow_logger.debug(f"receive get a template request, task_id is:{template_id}")
        template = TemplateManager.get(template_id)
        return get_json_result(data=template)

    @ns.expect(template_base_fields)
    @ns.marshal_with(custom_response())
    def put(self, template_id: str):
        """Update a specified template."""
        flow_logger.debug(
            f"receive get a template:{template_id} update request:{request.json}"
        )
        TemplateManager.update(
            template_id=template_id,
            name=request.json.get("name", ""),  # type: ignore
            image_url=request.json.get("image_url", ""),  # type: ignore
            remark=request.json.get("remark", ""),  # type: ignore
            workdir=request.json.get("workdir", ""),  # type: ignore
            command=request.json.get("command", []),  # type: ignore
            hyper_parameter=request.json.get("hyper_parameter", []),  # type: ignore
        )
        return get_json_result()

    @ns.marshal_with(custom_response())
    def delete(self, template_id: str):
        """Delete a specified template."""
        flow_logger.debug(f"receive get a template:{template_id} delete request")
        TemplateManager.delete(template_id)
        return get_json_result()
