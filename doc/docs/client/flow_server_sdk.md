## Introduction

We will describe how to use the `flow_server_sdk` sdk library to interact with `iflearner_flow_server` service.

## Installation
You can execute the following command to quickly install:
```shell
pip install iflearner-flow-client
```
Then you can reference the `flow_server_sdk` library for interface calls

## Initialization

We need to initialize the operation first, mainly to complete the relevant parameters of configuring the connection service, and generate a client object.

**Parameters**

| parameter |required | type | description |
| :------------- | :--- | :----- | --------------------- ---------------------------------------- |
| host | yes | string | The host for connecting `iflearner_flow_server` server |
| port| yes | string | The port for connecting `iflearner_flow_server` server |

**Usage**
```shell
from flow_server_sdk import FlowServerSdk
# use real ip address to initialize SDK
flow_server_client = FlowServerSdk(host="127.0.0.1", port="1235")
```

--8<--
client/sdk/flow_server/template.md
client/sdk/flow_server/task.md
--8<--