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
import argparse

from iflearner_flow_server.models.models import models_init
from iflearner_flow_server.routes import routes_init
from iflearner_job import iflearner_job

app, socketio = routes_init()
models_init(app)
iflearner_job.init_client()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start iflearner-flow server app")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="The host of flask app server",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=1235,
        help="The port of flask app server",
    )
    args = parser.parse_args()
    socketio.run(app=app, host=args.host, port=args.port)
