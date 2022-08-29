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
from flow_federate_sdk.api import flow_federate_api_base


class TaskManager(object):
    task_uri = "/api/v1/task"

    @classmethod
    @property
    def base_url(cls) -> str:
        return f"{flow_federate_api_base.generate_base_url(cls.task_uri)}"

    @classmethod
    def create(cls):
        pass

    @classmethod
    def update(cls):
        pass

    @classmethod
    def get(cls):
        pass

    @classmethod
    def list(cls):
        pass

    @classmethod
    def delete(cls):
        pass

    @classmethod
    def start(cls):
        pass

    @classmethod
    def stop(cls):
        pass
