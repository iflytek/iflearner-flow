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
"""Federate Manager, include the members of federate, the status of
federate."""


class FederateManager(object):
    @classmethod
    def register(cls, federate_name: str):
        """Federate member register.

        Args:
            federate_name (str): The name of federate.

        Returns:
        """
        pass

    @classmethod
    def unregister(cls, federate_name: str):
        """Federate member unregister.

        Args:
            federate_name (str): The name of federate.

        Returns:
        """
        pass

    @classmethod
    def list(cls, keyword: str, page: int = 1, limit: int = 10) -> list:
        """List federate members.

        Args:
            keyword (str): Keywords for fuzzy query.
            page (int): Current page number for query.
            limit (int): Limit Size for current page query.

        Returns:
            (list): The list of federate member.
        """
        pass
