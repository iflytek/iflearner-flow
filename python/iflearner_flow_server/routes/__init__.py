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
import importlib
import re
from pathlib import Path

from flask import Blueprint
from iflearner_flow_server.routes.api import app, blueprint, socketio


def auto_register_blue_print(app):
    for path in Path(__file__).parent.glob("*_route.py"):
        page_name = re.sub("$%s" % "_route", "", path.stem)
        module_name = ".".join(
            path.parts[path.parts.index("iflearner_flow_server") : -1] + (page_name,)
        )
        auto_blueprint = importlib.import_module(module_name)
        auto_blueprint.blue_route = Blueprint(page_name, module_name)
        app.register_blueprint(auto_blueprint.blue_route, url_prefix=f"/{page_name}")


app.register_blueprint(blueprint)
auto_register_blue_print(app)


def routes_init():
    return app, socketio
