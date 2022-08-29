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
"""flow server template operation command."""
import click
from flow_server_cli.utils.base_utils import PythonLiteralOption, flow_sdk, secho

template_id = click.option(
    "-id", "--template_id", type=click.STRING, required=True, help="The id of template"
)
template_name = click.option(
    "-n",
    "--template_name",
    type=click.STRING,
    required=True,
    help="The name of template",
)
remark = click.option(
    "-r",
    "--remark",
    type=click.STRING,
    required=False,
    default="",
    help="The remark of template",
)
image_url = click.option(
    "-i",
    "--image_url",
    type=click.STRING,
    required=True,
    help="The image url of template",
)
workdir = click.option(
    "-w",
    "--workdir",
    type=click.STRING,
    required=False,
    default="",
    help="The workdir of template",
)
command = click.option(
    "-c",
    "--command",
    cls=PythonLiteralOption,
    required=False,
    help='The command of template, such as ["python", "run.py"]',
    default="[]",
)
hyper_parameter = click.option(
    "-hp",
    "--hyper_parameter",
    cls=PythonLiteralOption,
    required=False,
    help='The hyper_parameter of template, such as ["ecoch=1"]',
    default="[]",
)

page = click.option(
    "-p",
    "--page",
    type=click.INT,
    required=False,
    default=1,
    help="The current page for list template query",
)
limit = click.option(
    "-l",
    "--limit",
    type=click.INT,
    required=False,
    default=10,
    help="The limit for list template query under current page",
)


@click.group(short_help="Template Operations Group")
@click.pass_context
def template(ctx):
    """\b Provides numbers of job operational commands, including create,
    update, query, list, delete, etc.

    For more details, please check out the help text.
    """
    pass


@template.command("create", short_help="Create Template Command")
@template_name
@remark
@image_url
@workdir
@command
@hyper_parameter
@click.pass_context
def create(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      create a template for task.
    \b
    - USAGE:
      flow_server_cli template create -n template_01 -r 'ocr template' -i pytorch_ocr:latest -w /data/ocr -c '["python", "run.py"]' -hp '["epoch=1"]'
    """
    resp = flow_sdk(ctx=ctx).template.create(
        name=kwargs["template_name"],
        remark=kwargs["remark"],
        image_url=kwargs["image_url"],
        workdir=kwargs["workdir"],
        command=kwargs["command"],
        hyper_parameter=kwargs["hyper_parameter"],
    )
    secho(resp)


@template.command("update", short_help="Update Template Command")
@template_id
@template_name
@remark
@image_url
@workdir
@command
@hyper_parameter
@click.pass_context
def update(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      update a template.
    \b
    - USAGE:
      flow_server_cli template update -id 9942183d92bd4c8d9d9d30d1a74f7b -n template_01 -r 'ocr template' -i pytorch_ocr:latest -w /data/ocr -c '["python", "run.py"]' -hp '["epoch=1"]'
    """
    resp = flow_sdk(ctx=ctx).template.update(
        template_id=kwargs["template_id"],
        name=kwargs["template_name"],
        remark=kwargs["remark"],
        image_url=kwargs["image_url"],
        workdir=kwargs["workdir"],
        command=kwargs["command"],
        hyper_parameter=kwargs["hyper_parameter"],
    )
    secho(resp)


@template.command("get", short_help="Get Template Command")
@template_id
@click.pass_context
def get(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      get a template.
    \b
    - USAGE:
      flow_server_cli template get -id 9942183d92bd4c8d9d9d30d1a74f7b
    """
    resp = flow_sdk(ctx=ctx).template.get(template_id=kwargs["template_id"])
    secho(resp)


@template.command("list", short_help="List Templates Command")
@page
@limit
@click.pass_context
def list(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      list template by query params.
    \b
    - USAGE:
      flow_server_cli template list -p 1 -l 10
    """
    resp = flow_sdk(ctx=ctx).template.list(limit=kwargs["limit"], page=kwargs["page"])
    secho(resp)


@template.command("delete", short_help="Delete Templates Command")
@template_id
@click.pass_context
def delete(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      delete a template.
    \b
    - USAGE:
      flow_server_cli template delete -id 9942183d92bd4c8d9d9d30d1a74f7b
    """
    resp = flow_sdk(ctx=ctx).template.delete(template_id=kwargs["template_id"])
    secho(resp)
