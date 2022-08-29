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
import os
import json

import click
import yaml
from flow_server_cli.command import template, task
from flow_server_cli.utils.base_utils import secho

@click.group(
    short_help="Iflearner Server Flow Cli",
    context_settings=dict(help_option_names=["-h", "--help"]),
)
@click.pass_context
def flow_cli(ctx):
    """Iflearner Flow Server  Cli."""
    ctx.ensure_object(dict)
    if ctx.invoked_subcommand == "init":
        return
    with open(
        os.path.join(os.path.dirname(__file__), "flow_server_conf.yaml"), "r"
    ) as fin:
        conf_dict = yaml.safe_load(fin)
    ctx.obj["host"] = conf_dict["host"]
    ctx.obj["port"] = conf_dict["port"]


@flow_cli.command("init", short_help="Iflearner Server Flow Cli Init Command")
@click.option(
    "--host",
    type=click.STRING,
    required=False,
    default="127.0.0.1",
    help="The host of iflearner flow server",
)
@click.option(
    "--port",
    type=click.INT,
    required=False,
    default=1235,
    help="The port of iflearner flow server",
)
@click.pass_context
def init(ctx, **kwargs):
    """
    \b
    - DESCRIPTION:
        Iflearner Flow Server Cli Init Command.
    \b
    - USAGE:
        flow_server_cli init --host 127.0.0.1 --port 1235
    """
    conf_dict = {"host": kwargs["host"], "port": kwargs["port"]}
    with open(
        os.path.join(os.path.dirname(__file__), "flow_server_conf.yaml"), "w"
    ) as fout:
        yaml.dump(
            conf_dict, fout, default_flow_style=False, allow_unicode=True, indent=4
        )
    secho({"ret_code": 0, "ret_message": "success"})


flow_cli.add_command(template.template)
flow_cli.add_command(task.task)


if __name__ == "__main__":
    flow_cli()
