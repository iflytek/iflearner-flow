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
from setuptools import find_packages, setup


def _process_requirements():
    packages = open('requirements.txt').read().strip().split('\n')
    requires = []
    for pkg in packages:
        if pkg.startswith('git+ssh'):
            return_code = os.system('pip install {}'.format(pkg))
            assert return_code == 0, 'error, status_code is: {}, exit!'.format(return_code)
        else:
            requires.append(pkg)
    return requires

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="iflearner-flow-client",
    version="0.2.0",
    description="Iflearner Flow Client, include flow_server_sdk, flow_federate_client, flow_server_cli, flow_federate_cli",
    author="The iFLYTEK Turing Group",
    url="https://github.com/iflytek/iflearner-flow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    entry_points={
        "console_scripts": [
            "flow_server_cli = flow_server_cli.flow_cli:flow_cli",
            "flow_federate_cli = flow_federate_cli.flow_cli:flow_cli",
        ]
    },
    packages=[
        package for package in find_packages()
        if package.startswith('flow')
    ],
    install_requires=_process_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires='>=3.7',
)
