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
import click
from flow_federate_cli.utils.base_utils import secho

task_id = click.option(
    "-id", "--template_id", type=click.STRING, required=True, help="The id of task"
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


@click.group(short_help="Task Operations Group")
@click.pass_context
def task(ctx):
    """\b Provides numbers of task operational commands, including get, list,
    stop, etc.

    For more details, please check out the help text.
    """
    pass


@task.command("get", short_help="Get Task Command")
@task_id
@click.pass_context
def get(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      get a task.
    \b
    - USAGE:
      flow_federate_cli task get -id 9942183d92bd4c8d9d9d30d1a74f7b
    """
    secho({"test": 111})
    pass


@task.command("list", short_help="List Task Command")
@page
@limit
@click.pass_context
def list(ctx, **kwargs):
    """
    - DESCRIPTION:\n
    \b
      list task by query params.
    \b
    - USAGE:
      flow_federate_cli template list -p 1 -l 10
    """
    # resp = flow_sdk(ctx=ctx).task.list(limit=kwargs['limit'], page=kwargs['page'])
    # secho(resp)
    pass
