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
from typing import Any, Dict

import requests

__all__ = ["get", "post", "delete", "put"]

json_head = {"Content-Type": "application/json;charset=UTF-8"}


def post(url: str, data=None, headers=json_head, files=None, enable_json=True) -> Any:
    """Sends a POST request
    Args:
        url (str): The url for request.
        data: The data for request.
        headers (dict): The head for request.
        files: The file for request.
        enable_json (bool): Enable json.
    Returns:
    """
    sess = requests.Session()
    if enable_json:
        r = sess.post(url=url, json=data, headers=headers, files=files)
    else:
        r = sess.post(url=url, data=data, headers=headers, files=files)
    r.raise_for_status()
    return r.json()


def get(
    url: str,
    param: Dict[str, Any] = None,
    headers=json_head,
    data=None,
    enable_json=True,
):
    """Sends a GET request
    Args:
        url (str): The url for request.
        param (Dict[str, Any]): The param for request.
        headers (dict): The header for request.
        data: The data for request.
        enable_json (bool): Enable json.
    """
    sess = requests.Session()
    if enable_json:
        r = sess.get(url=url, params=param, headers=headers, json=data)
    else:
        r = sess.get(url=url, params=param, headers=headers, data=data)
    r.raise_for_status()
    return r.json()


def put(url: str, data=None, headers=json_head, enable_json=True) -> Any:
    """Sends a PUT request
    Args:
        url (str): The url for request.
        data: The data for request.
        headers (dict): The header for request.
        enable_json (bool): Enable json.
    Returns:
    """
    sess = requests.Session()
    if enable_json:
        r = sess.put(url=url, json=data, headers=headers)
    else:
        r = sess.put(url=url, data=data, headers=headers)
    r.raise_for_status()
    return r.json()


def delete(url: str, data=None, headers=json_head, enable_json=True) -> Any:
    """Sends a DELETE request
    Args:
        url (str): The url for request.
        data: The data for request.
        headers (dict): The head for request.
        enable_json (bool): Enable json.
    Returns:
    """
    sess = requests.Session()
    if enable_json:
        r = sess.delete(url=url, json=data, headers=headers)
    else:
        r = sess.delete(url=url, data=data, headers=headers)
    r.raise_for_status()
    return r.json()
