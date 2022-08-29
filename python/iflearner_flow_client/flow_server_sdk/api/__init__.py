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
from flow_server_sdk.utils.base_utils import Singleton


@Singleton
class FlowServerApiBase(object):
    def __init__(self):
        self._flow_server_addr = "127.0.0.1:1235"

    @property
    def flow_server_addr(self) -> str:
        return self._flow_server_addr

    def init(self, host: str, port: int):
        self._flow_server_addr = f"{host}:{port}"

    def generate_base_url(self, uri: str):
        return f"http://{self._flow_server_addr}{uri}"


flow_server_api_base = FlowServerApiBase()
