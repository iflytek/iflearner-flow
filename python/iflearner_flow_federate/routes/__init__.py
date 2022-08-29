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
from iflearner_flow_federate.routes.api import app, blueprint, sio, socketio_namespace
from iflearner_flow_federate.utils.conf import conf_inst


def auto_register_blue_print(app):
    for path in Path(__file__).parent.glob("*_route.py"):
        page_name = re.sub("$%s" % "_route", "", path.stem)
        module_name = ".".join(
            path.parts[path.parts.index("iflearner_flow_federate") : -1] + (page_name,)
        )
        auto_blueprint = importlib.import_module(module_name)
        auto_blueprint.blue_route = Blueprint(page_name, module_name)
        app.register_blueprint(auto_blueprint.blue_route, url_prefix=f"/{page_name}")


app.register_blueprint(blueprint)
auto_register_blue_print(app)


def register():
    sio.connect(
        f"http://{conf_inst.flow_conf.federate_server_addr}",
        namespaces=[socketio_namespace],
    )
    sio.sleep(2)
    sio.emit(
        "register",
        {
            "id": conf_inst.flow_conf.federate_id,
            "name": conf_inst.flow_conf.federate_id,
            "host": conf_inst.flow_conf.federate_host,
        },
        namespace=socketio_namespace,
    )


def routes_init():
    register()
    return app
