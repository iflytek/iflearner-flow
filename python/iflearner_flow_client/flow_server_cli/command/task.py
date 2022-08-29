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
"""flow server task operation command."""
import click
from flow_server_cli.utils.base_utils import PythonLiteralOption, flow_sdk, secho

task_id = click.option(
    "-id", 
    "--task_id", 
    type=click.STRING, 
    required=True, 
    help="The id of task"
)
task_name = click.option(
    "-n",
    "--task_name",
    type=click.STRING,
    required=True,
    help="The name of task",
)
template_id = click.option(
    "-t",
    "--template_id",
    type=click.STRING,
    required=True,
    help="The id of template",
)
remark = click.option(
    "-r",
    "--remark",
    type=click.STRING,
    required=False,
    default="",
    help="The remark of task",
)
federate_data = click.option(
    "-fd",
    "--federate_data",
    cls=PythonLiteralOption,
    required=True,
    help="The mapping data of federate members",
)
page = click.option(
    "-p",
    "--page",
    type=click.INT,
    required=False,
    default=1,
    help="The current page for list task query",
)
limit = click.option(
    "-l",
    "--limit",
    type=click.INT,
    required=False,
    default=10,
    help="The limit for list task query under current page",
)

@click.group(short_help="Task Operations Group")
@click.pass_context
def task(ctx):
    """\b Provides numbers of job operational commands, including create,
    update, query, list, delete, etc.

    For more details, please check out the help text.
    """
    pass

@task.command("create", short_help="Create Task Command")
@task_name
@template_id
@remark
@federate_data
@click.pass_context
def create(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      create task
    \b
    - USAGE:
      flow_server_cli task create -n task01 -t ea0f10bfbaf64a74a061d54c94cc69 -r "This is a remark." -fd '[{"federated_id": "federate-1", "federated_data": ""}]'
    """
    resp = flow_sdk(ctx=ctx).task.create(
        name=kwargs["task_name"],
        template_id=kwargs["template_id"],
        remark=kwargs["remark"],
        federate_data=kwargs["federate_data"],
    )
    secho(resp)

@task.command("update", short_help="Update Task Command")
@task_id 
@task_name
@template_id
@remark
@federate_data
@click.pass_context
def update(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      update task
    \b
    - USAGE:
      flow_server_cli task update -id bbc0c30e96bc4da29b2b326fb1f8786e -n task01 -t ea0f10bfbaf64a74a061d54c94cc69 -r "This is a new remark." -fd '[{"federated_id": "federate-1", "federated_data": ""}]'
    """
    resp = flow_sdk(ctx=ctx).task.update(
        task_id=kwargs["task_id"],
        name=kwargs["task_name"],
        template_id=kwargs["template_id"],
        remark=kwargs["remark"],
        federate_data=kwargs["federate_data"],
    )
    secho(resp)

@task.command("get", short_help="Get Task Command")
@task_id 
@click.pass_context
def get(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      get task details
    \b
    - USAGE:
      flow_server_cli task get -id bbc0c30e96bc4da29b2b326fb1f8786e
    """
    resp = flow_sdk(ctx=ctx).task.get(
        task_id=kwargs["task_id"],
    )
    secho(resp)

@task.command("list", short_help="List Task Command")
@page
@limit
@click.pass_context
def list(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      list task
    \b
    - USAGE:
      flow_server_cli task list -p 1 -l 5
    """
    resp = flow_sdk(ctx=ctx).task.list(
        page=kwargs["page"],
        limit=kwargs["limit"],
    )
    secho(resp)

@task.command("delete", short_help="Delete Task Command")
@task_id 
@click.pass_context
def delete(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      delete task
    \b
    - USAGE:
      flow_server_cli task delete -id bbc0c30e96bc4da29b2b326fb1f8786e
    """
    resp = flow_sdk(ctx=ctx).task.delete(
        task_id=kwargs["task_id"],
    )
    secho(resp)

@task.command("start", short_help="Start Task Command")
@task_id 
@click.pass_context
def start(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      start task
    \b
    - USAGE:
      flow_server_cli task start -id bbc0c30e96bc4da29b2b326fb1f8786e
    """
    resp = flow_sdk(ctx=ctx).task.start(
        task_id=kwargs["task_id"],
    )
    secho(resp)

@task.command("stop", short_help="Stop Task Command")
@task_id 
@click.pass_context
def stop(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      stop task
    \b
    - USAGE:
      flow_server_cli task stop -id bbc0c30e96bc4da29b2b326fb1f8786e
    """
    resp = flow_sdk(ctx=ctx).task.stop(
        task_id=kwargs["task_id"],
    )
    secho(resp)
