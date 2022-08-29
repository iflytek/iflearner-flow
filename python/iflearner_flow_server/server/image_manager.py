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
"""Image manager."""
from typing import Generator, Union

import docker


class DockerClient(object):
    def __init__(
        self,
        auto: bool = True,
        base_url: str = "unix:///var/run/docker.sock",
        version: str = "auto",
        max_pool_size: int = 10,
        timeout: int = 600,
    ):
        """
        Args:
            auto (bool): Init docker client from environment variables automatically when auto is True, else Please configure
             other parameters。
            base_url (str): URL to the Docker server. For example, unix:///var/run/docker.sock or tcp://127.0.0.1:1234.
            version (str): The version of the API to use. Set to auto to automatically detect the server’s version. Default: 1.35
            max_pool_size (int): The maximum number of connections to save in the pool.
            timeout (int): Default timeout for API calls, in seconds.
        """
        self._docker_client: docker.DockerClient = None
        if auto:
            self._docker_client = docker.from_env()
        else:
            self._docker_client = docker.DockerClient(
                base_url=base_url,
                version=version,
                max_pool_size=max_pool_size,
                timeout=timeout,
            )
        version_info: dict = self._docker_client.version()
        print(f"docker version info is:{version_info}")

    @property
    def docker_client(self) -> docker.DockerClient:
        return self._docker_client

    def ping(self) -> bool:
        """Ping Docker server."""
        return self._docker_client.ping()

    def login(
        self,
        username,
        password=None,
        email=None,
        registry=None,
        reauth=False,
        dockercfg_path=None,
    ) -> dict:
        """Authenticate with a registry. Similar to the ``docker login``
        command.

        Args:
            username (str): The registry username
            password (str): The plaintext password
            email (str): The email for the registry account
            registry (str): URL to the registry.  E.g.
                ``https://index.docker.io/v1/``
            reauth (bool): Whether or not to refresh existing authentication on
                the Docker server.
            dockercfg_path (str): Use a custom path for the Docker config file
                (default ``$HOME/.docker/config.json`` if present,
                otherwise ``$HOME/.dockercfg``)

        Returns:
            (dict): The response from the login request
        """
        return self._docker_client.login(
            username=username,
            password=password,
            email=email,
            registry=registry,
            reauth=reauth,
            dockercfg_path=dockercfg_path,
        )


class ImageBase(object):
    @classmethod
    def list_images(
        cls, docker_client: docker.DockerClient, name=None, all=False, filters=None
    ) -> docker.DockerClient.images:
        """List images.

        Args:
            docker_client: The Docker client instance.
            name (str): Only show images belonging to the repository ``name``
            all (bool): Show intermediate image layers. By default, these are
                filtered out.
            filters (dict): Filters to be processed on the image list.
                Available filters:
                - ``dangling`` (bool)
                - `label` (str|list): format either ``"key"``, ``"key=value"``
                    or a list of such.
        Returns:
            (list of :py:class:`docker.Image`): The images.
        """
        images = docker_client.images.list(name=name, all=all, filters=filters)
        return images

    @classmethod
    def get_image(cls, docker_client: docker.DockerClient, name: str):
        """Gets an image by name.

        Args:
            docker_client: The Docker client instance.
            name (str): The name of the image.

         Example:
            >>> image = ImageBase().get_image(docker_client, 'python:3.7')
            ... print(image.tags)
            ['python:3.7', 'registry.turing.com/test/python:3.7']
            ...
        """
        return docker_client.images.get(name=name)

    @classmethod
    def push_image(
        cls,
        docker_client: docker.DockerClient,
        repository: str,
        tag: str = None,
        stream: bool = False,
        auth_config=None,
        decode: bool = False,
    ) -> Union[Generator, str]:
        """Push an image or a repository to the registry. Similar to the
        ``docker push`` command.

        Args:
            docker_client: The Docker client instance.
            repository (str): The repository to push to
            tag (str): An optional tag to push
            stream (bool): Stream the output as a blocking generator
            auth_config (dict): Override the credentials that are found in the
                config for this request.  ``auth_config`` should contain the
                ``username`` and ``password`` keys to be valid.
            decode (bool): Decode the JSON data from the server into dicts.
                Only applies with ``stream=True``

        Returns:
             (generator or str): The output from the server.

        Example:
            >>> for line in ImageBase().push_image(docker_client, 'yourname/app', stream=True, decode=True):
            ...   print(line)
            {'status': 'Pushing repository yourname/app (1 tags)'}
            {'status': 'Pushing','progressDetail': {}, 'id': '511136ea3c5a'}
            {'status': 'Image already pushed, skipping', 'progressDetail':{},
             'id': '511136ea3c5a'}
            ...
        """
        return docker_client.images.push(
            repository=repository,
            tag=tag,
            stream=stream,
            auth_config=auth_config,
            decode=decode,
        )

    @classmethod
    def pull_image(
        cls,
        docker_client: docker.DockerClient,
        repository: str,
        tag: str = None,
        all_tags: bool = False,
    ):
        """Gets an image by name. Pull an image of the given name and return
        it. Similar to the ``docker pull`` command.

        If ``tag`` is ``None`` or empty, it is set to ``latest``.
        If ``all_tags`` is set, the ``tag`` parameter is ignored and all image
        tags will be pulled.

        Args:
            docker_client: The Docker client instance.
            repository (str): The repository to pull
            tag (str): The tag to pull
            all_tags (bool): Pull all image tags
        """
        return docker_client.images.pull(
            repository=repository, tag=tag, all_tags=all_tags
        )


if __name__ == "__main__":
    docker_client_conn = DockerClient(auto=True).docker_client

    ImageBase().list_images(docker_client_conn)

    ImageBase().get_image(docker_client_conn, "python:3.7")
