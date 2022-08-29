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

import json
import warnings
from typing import List
import unittest
from flow_server_sdk import FlowServerSdk

class Task(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.flow_server_client = FlowServerSdk(host="127.0.0.1", port="1235")

    def test_create(self):
        resp = self.flow_server_client.task.create(
            name="testCase1", 
            template_id="ea0f10bfbaf64a74a061d54c94cc69", 
            remark="This is a remark.", 
            federate_data=[{"federated_id": "federate-1", "federated_data": ""}],
        )
        print(json.dumps(resp, indent=4, sort_keys=True))

    def test_update(self):
        resp = self.flow_server_client.task.update(
            task_id="0578abed1032425499abd20f2ef67938", 
            name="testCase", 
            template_id="ea0f10bfbaf64a74a061d54c94cc69", 
            remark="This is a remark.", 
            federate_data=[{"federated_id": "federate-1", "federated_data": "aa"}],
        )
        print(json.dumps(resp, indent=4, sort_keys=True))

    def test_get(self):
        resp = self.flow_server_client.task.get("0578abed1032425499abd20f2ef67938")
        print(json.dumps(resp, indent=4, sort_keys=True))

    def test_list(self):
        resp = self.flow_server_client.task.list(
            page=1, 
            limit=10,
        )
        print(json.dumps(resp, indent=4, sort_keys=True))

    def test_delete(self):
        resp = self.flow_server_client.task.delete("5986dd8986654fa6af3404a1d1eada72")
        print(resp)

    def test_start(self):
        resp = self.flow_server_client.task.start("31b11982")
        print(resp)

    def test_stop(self):
        resp = self.flow_server_client.task.stop("31b11982")
        print(resp)


if __name__ == "__main__":
    unittest.main()
