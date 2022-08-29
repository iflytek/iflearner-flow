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
import unittest
import uuid
import warnings

from flow_server_sdk import FlowServerSdk


class Template(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.flow_server_client = FlowServerSdk(host="127.0.0.1", port="1235")
        resp = self.flow_server_client.template.create(
            name=str(uuid.uuid4()),
            image_url="iflearner_ocr:0.0.1",
            workdir="/data/ocr/script",
            command=[],
        )
        self.assertEqual(resp["ret_code"], 0)
        self._generate_template_id = resp["data"]["template_id"]

    def test_0_create(self):
        resp = self.flow_server_client.template.create(
            name="",
            image_url="iflearner_ocr:0.0.1",
            workdir="/data/ocr/script",
            command=[],
        )
        self.assertNotEqual(resp["ret_code"], 0)

    def test_1_update(self):
        resp = self.flow_server_client.template.update(
            template_id=self._generate_template_id,
            name=str(uuid.uuid4()),
            image_url="iflearner_ocr:0.0.2",
            workdir="/data/ocr/script",
            command=[],
        )
        self.assertEqual(resp["ret_code"], 0)
        resp = self.flow_server_client.template.update(
            template_id=self._generate_template_id,
            name="",
            image_url="iflearner_ocr:0.0.1",
            workdir="/data/ocr/script",
            command=[],
        )
        self.assertNotEqual(resp["ret_code"], 0)
        resp = self.flow_server_client.template.update(
            template_id=str(uuid.uuid4()),
            name="123",
            image_url="iflearner_ocr:0.0.1",
            workdir="/data/ocr/script",
            command=[],
        )
        self.assertNotEqual(resp["ret_code"], 0)

    def test_2_get(self):
        resp = self.flow_server_client.template.get(
            template_id=self._generate_template_id
        )
        self.assertEqual(resp["ret_code"], 0)
        resp = self.flow_server_client.template.get(template_id=str(uuid.uuid4()))
        self.assertNotEqual(resp["ret_code"], 0)

    def test_3_list(self):
        resp = self.flow_server_client.template.list(keyword="", page=1, limit=10)
        self.assertEqual(resp["ret_code"], 0)

    def test_4_delete(self):
        resp = self.flow_server_client.template.delete(
            template_id=self._generate_template_id
        )
        self.assertEqual(resp["ret_code"], 0)
        resp = self.flow_server_client.template.delete(template_id=str(uuid.uuid4()))
        self.assertNotEqual(resp["ret_code"], 0)


if __name__ == "__main__":
    unittest.main()
