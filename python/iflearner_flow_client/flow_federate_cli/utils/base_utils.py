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
import ast
import json
import os
from typing import Any, Dict, List, Tuple

import click
from flow_federate_sdk import FlowFederateSdk


class ConvertStrToList(click.Option):
    def type_cast_value(self, ctx, value) -> List:
        try:
            value = str(value)
            assert value.count("[") == 1 and value.count("]") == 1
            list_as_str = value.replace('"', "'").split("[")[1].split("]")[0]
            list_of_items = [item.strip().strip("'") for item in list_as_str.split(",")]
            return list_of_items
        except Exception:
            raise click.BadParameter(value)


class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except Exception:
            raise click.BadParameter(value)


def get_env_vars(ctx, args, incomplete):
    return [k for k in os.environ.keys() if incomplete in k]


def secho(resp: Dict[str, Any]):
    if resp["ret_code"] == 0:
        click.secho(json.dumps(resp, indent=2), fg="blue")
    else:
        click.secho(json.dumps(resp, indent=2), fg="red")


def get_addr(ctx) -> Tuple[str, str]:
    return ctx.obj["host"], ctx.obj["port"]


def flow_sdk(ctx) -> FlowFederateSdk:
    host, port = get_addr(ctx)
    return FlowFederateSdk(host=host, port=port)
