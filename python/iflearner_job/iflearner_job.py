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
import typing

import requests
from kubernetes import client, config

Role = str
RoleServer = "server"
RoleClient = "client"

IflearnerJobStatus = str
IflearnerJobStarted = "Started"
IflearnerJobPending = "Pending"
IflearnerJobRunning = "Running"
IflearnerJobSucceeded = "Succeeded"
IflearnerJobFailed = "Failed"
IflearnerJobUnknown = "Unknown"
IflearnerJobCancelled = "Cancelled"

IflearnerJobException = client.ApiException

MountPath = "/data"

StatusPort = 82

def init_client():
    config.load_config()
    global api
    api = client.CustomObjectsApi()


def _catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args)
        except client.ApiException as e:
            raise e

    return wrapper


def is_active(status: IflearnerJobStatus) -> bool:
    if status in {
        IflearnerJobStarted,
        IflearnerJobPending,
        IflearnerJobRunning,
        IflearnerJobUnknown,
    }:
        return True

    return False


class IflearnerJob:
    def __init__(self, uuid: str, role: Role) -> None:
        self._group = "git.iflytek.com"
        self._version = "v1"
        self._namespace = "default"
        self._plural = "iflearnerjobs"
        self._body = {"apiVersion": "git.iflytek.com/v1", "kind": "IflearnerJob"}
        self._uuid = uuid
        self._role = role

    def _generate_name(self) -> str:
        if self._role == RoleClient:
            return "iflearnerjob-client-" + self._uuid
        else:
            return "iflearnerjob-server-" + self._uuid

    @_catch_exception
    def create(
        self, 
        image: str, 
        working_dir: str, 
        args: typing.List[str], 
        subdomain: str = None, 
        volume: str = None,
        other_parties: typing.List[str] = None,
    ):
        """Create job.

        Args:
            image: The image used by container.
            working_dir: Container working directory.
            args: Container running arguments.
            subdomain: Party uses the subdomain to request the server.
            volume: The path of volume.
            other_parties: When using SMPC, you need to specify the addresses of other parties.
        """

        name = self._generate_name()
        if subdomain is None:
            host = self._uuid + ".server.iflearner.com"
        else:
            host = subdomain + ".server.iflearner.com"
        self._body["metadata"] = client.V1ObjectMeta(name=name).to_dict()
        spec = {"role": self._role, "host": host}

        container = client.V1Container(
            image=image,
            name=name,
            image_pull_policy="IfNotPresent",
            working_dir=working_dir,
        )

        volume_mount_name = ""
        if self._role == RoleClient:
            args.append(f"--server={host}:30031")
            args.append("--cert=/etc/server-iflearner-secret.crt")
            if volume is not None and volume != "":
                volume_mount_name = name
                container.volume_mounts = [client.V1VolumeMount(mount_path=MountPath, name=volume_mount_name)]
            if other_parties != None and len(other_parties) > 0:
                peers = ";".join(other_parties)
                args.append(f"--peers=0.0.0.0:50001;{peers}")
                args.append("--peer-cert=/etc/party-iflearner-secret.crt")

        # else:
        #     # args.append("--addr=0.0.0.0:50051")
        #     container.ports = [client.V1ContainerPort(container_port=StatusPort)]

        container.args = args
        temp = client.V1PodTemplateSpec(
            spec=client.V1PodSpec(
                restart_policy="Never", 
                containers=[container], 
            ),
        )
        if volume_mount_name != "":
            temp.spec.volumes = [client.V1Volume(
                name=volume_mount_name,
                host_path=client.V1HostPathVolumeSource(path=volume, type="Directory"),
            )]
        spec["template"] = temp
        self._body["spec"] = spec  # type: ignore
        api.create_namespaced_custom_object(  # type: ignore
            self._group, self._version, self._namespace, self._plural, self._body
        )

    @_catch_exception
    def delete(self):
        """Delete job.
        """

        name = self._generate_name()
        api.delete_namespaced_custom_object(
            self._group, self._version, self._namespace, self._plural, name
        )  # type: ignore

    @_catch_exception
    def status(self) -> IflearnerJobStatus:
        """Get current status of job.

        Returns:
            Extract status from custom object status.
        """

        name = self._generate_name()
        custom_object = api.get_namespaced_custom_object_status(  # type: ignore
            self._group, self._version, self._namespace, self._plural, name
        )
        if "status" in custom_object:
            if custom_object["status"]["phase"] == IflearnerJobRunning:
                # TODO: get status from iflearner-operator
                pass

            return custom_object["status"]["phase"]

        return IflearnerJobUnknown

    @_catch_exception
    def client_status(self) -> typing.List:
        """Call aggregation server to get the status of the parties.

        Returns:
            The list of parties.
        """

        if self._role == RoleServer:
            try:
                name = self._generate_name()
                resp = requests.get(f"http://{name}.{self._namespace}:{StatusPort}/v1/status", timeout=3)
                if resp.status_code == 200:
                    content = json.loads(resp.content)
                    parties = []
                    for k, v in content.items():
                        v["name"] = k
                        parties.append(v)

                    return parties
            except Exception as e:
                raise IflearnerJobException(reason=e)

        return []

    @_catch_exception
    def logs(self) -> str:
        """Get job logs.

        Returns:
            The string of logs.
        """

        logs = client.CoreV1Api().read_namespaced_pod_log(
            self._generate_name(), self._namespace
        )

        return logs


class ClientStatus:
    def __init__(
        self, ready: bool, complete: bool, current_epoch: int, total_epoch: int
    ) -> None:
        self.ready = ready
        self.complete = complete
        self.current_epoch = current_epoch
        self.total_epoch = total_epoch
