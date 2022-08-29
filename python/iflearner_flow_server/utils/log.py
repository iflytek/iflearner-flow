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
"""Log module."""
import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Union

from iflearner_flow_server.utils.base_utils import Singleton
from iflearner_flow_server.utils.conf import conf_inst


class LogBase(object):
    def __init__(
        self,
        name: str,
        level: Union[str, int],
        enable_console: bool = True,
        enable_file: bool = False,
        log_path: str = "./log/log.log",
        max_bytes: int = 1024 * 1024 * 300,
        backup_count: int = 10,
        formatter: str = "%(asctime)s: %(name)s  %(levelname)s %(filename)s:%(lineno)d %(message)s",
    ):
        self._logger = logging.getLogger(name)
        formatter = logging.Formatter(formatter)  # type: ignore
        if enable_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level=level)
            console_handler.setFormatter(formatter)  # type: ignore
            self._logger.addHandler(console_handler)
        self._logger.propagate = False
        if enable_file:
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            file_log_handler = RotatingFileHandler(
                log_path, maxBytes=max_bytes, backupCount=backup_count
            )
            file_log_handler.setFormatter(formatter)  # type: ignore
            file_log_handler.setLevel(level=level)
            self._logger.addHandler(file_log_handler)
        self._logger.setLevel(level=level)

    def get_logger(self):
        return self._logger


@Singleton
class FlowLog(LogBase):
    pass


@Singleton
class SocketioLog(LogBase):
    pass


@Singleton
class SqlEngineLog(LogBase):
    pass


flow_logger = FlowLog(
    name="iflearner_flow",
    level=conf_inst.flow_log_conf.level,
    enable_file=conf_inst.flow_log_conf.enable_file,
    enable_console=conf_inst.flow_log_conf.enable_console,
    log_path=conf_inst.flow_log_conf.log_path,
).get_logger()

socketio_logger = SocketioLog(
    name="socketio",
    level=conf_inst.socket_io_log_conf.level,
    enable_file=conf_inst.socket_io_log_conf.enable_file,
    enable_console=conf_inst.socket_io_log_conf.enable_console,
    log_path=conf_inst.socket_io_log_conf.log_path,
).get_logger()

sqlengine_logger = SqlEngineLog(
    name="sqlalchemy.engine",
    level=conf_inst.sql_engine_log_conf.level,
    enable_file=conf_inst.sql_engine_log_conf.enable_file,
    enable_console=conf_inst.sql_engine_log_conf.enable_console,
    log_path=conf_inst.sql_engine_log_conf.log_path,
).get_logger()
