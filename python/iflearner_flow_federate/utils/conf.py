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
from typing import Any

import yaml
from iflearner_flow_federate.utils.base_utils import Singleton


def read_yaml(path: str) -> Any:
    with open(path, "rb") as f:
        cf = f.read()
    cf = yaml.load(cf, Loader=yaml.SafeLoader)
    return cf


class LogBaseConf(object):
    def __init__(
        self, level: str, enable_file: bool, enable_console: bool, log_path: str
    ):
        self._level = level
        self._enable_file = enable_file
        self._enable_console = enable_console
        self._log_path = log_path

    @property
    def level(self) -> str:
        return self._level

    @property
    def enable_file(self) -> bool:
        return self._enable_file

    @property
    def enable_console(self) -> bool:
        return self._enable_console

    @property
    def log_path(self) -> str:
        return self._log_path


class FlowConf(object):
    def __init__(self, federate_server_addr: str, federate_id: str, federate_name: str, federate_host: str):
        self._federate_server_addr = federate_server_addr
        self._federate_id = federate_id
        self._federate_name = federate_name
        self._federate_host = federate_host
        self._federate_server_http_uri = f"http://{federate_server_addr}/api/v1"

    @property
    def federate_server_http_uri(self) -> str:
        return self._federate_server_http_uri

    @property
    def federate_server_addr(self) -> str:
        return self._federate_server_addr

    @property
    def federate_id(self) -> str:
        return self._federate_id

    @property
    def federate_name(self) -> str:
        return self._federate_name

    @property
    def federate_host(self) -> str:
        return self._federate_host


@Singleton
class ConfParse(object):
    def __init__(self):
        self._raw_dict = None
        self._socket_io_log_conf = None
        self._sql_engine_log_conf = None
        self._flow_log_conf = None
        self._flow_conf = None

    def __call__(self, path: str):
        cf = read_yaml(path)
        self._raw_dict = cf
        flow_conf = cf.get("log").get("flow")
        self._flow_log_conf = LogBaseConf(
            level=flow_conf.get("level", "DEBUG"),
            enable_file=flow_conf.get("enable_file", True),
            enable_console=flow_conf.get("enable_console", True),
            log_path=flow_conf.get("log_path", "./log/flow.log"),
        )
        socket_io_log_conf = cf.get("log").get("sockeio")
        self._socket_io_log_conf = LogBaseConf(
            level=socket_io_log_conf.get("level", "INFO"),
            enable_file=socket_io_log_conf.get("enable_file", True),
            enable_console=socket_io_log_conf.get("enable_console", False),
            log_path=socket_io_log_conf.get("log_path", "./log/socket_io.log"),
        )

        sql_engine_log_conf = cf.get("log").get("sqlengine")
        self._sql_engine_log_conf = LogBaseConf(
            level=sql_engine_log_conf.get("level", "INFO"),
            enable_file=sql_engine_log_conf.get("enable_file", True),
            enable_console=sql_engine_log_conf.get("enable_console", False),
            log_path=sql_engine_log_conf.get("log_path", "./log/sql_engine.log"),
        )
        flow_conf = cf["flow"]
        self._flow_conf = FlowConf(
            federate_server_addr=flow_conf.get("federate_server_addr"),
            federate_name=flow_conf.get("federate_name"),
            federate_id=flow_conf.get("federate_id"),
            federate_host=flow_conf.get("federate_host"),
        )

    @property
    def raw_dict(self) -> dict:
        return self._raw_dict

    @property
    def flow_conf(self) -> FlowConf:
        return self._flow_conf

    @property
    def flow_log_conf(self) -> LogBaseConf:
        return self._flow_log_conf

    @property
    def socket_io_log_conf(self) -> LogBaseConf:
        return self._socket_io_log_conf

    @property
    def sql_engine_log_conf(self) -> LogBaseConf:
        return self._sql_engine_log_conf


conf_inst = ConfParse()
conf_inst(
    path=os.getenv("FLOW_FEDERATE_CONF_PATH", default="./conf/flow_federate_dev.yaml")
)
