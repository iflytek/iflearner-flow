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
from flow_server_sdk.api import flow_server_api_base
from flow_server_sdk.api.template import TemplateManager
from flow_server_sdk.api.task import TaskManager

__all__ = ["FlowServerSdk"]


class FlowServerSdk(object):
    template = TemplateManager()
    task = TaskManager()

    def __init__(self, host: str, port: int):
        flow_server_api_base.init(host=host, port=port)

    def set_addr(self, host: str, port: int):
        flow_server_api_base.init(host=host, port=port)
