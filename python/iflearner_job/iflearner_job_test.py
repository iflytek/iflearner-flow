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
import iflearner_job


def test_iflearner_job() -> None:
    iflearner_job.init_client()
    ifl_job = iflearner_job.IflearnerJob("s1", iflearner_job.RoleServer)
    # ifl_job.create("iflearner:0.1.1", None, ["python", "iflearner/business/homo/aggregate_server.py", "-n=1"])

    # ifl_job = iflearner_job.IflearnerJob("c1", iflearner_job.RoleClient)
    # ifl_job.create("iflearner:0.1.1", "/iflearner/examples/homo/quickstart_pytorch", ["python", "-u", "quickstart_pytorch.py", "--name=test", "--epochs=10"], "s1")

    try:
        print(ifl_job.status())
        print(ifl_job.logs())
    except iflearner_job.IflearnerJobException as e:
        print(e)


if __name__ == "__main__":
    test_iflearner_job()
