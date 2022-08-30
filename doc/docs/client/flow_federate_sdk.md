## flow_federate_sdk

## Introduction

We will describe how to use the `flow_federate_sdk` sdk library to interact with `iflearner_flow_federate` service.

## Installation
You can execute the following command to quickly install:
```shell
pip install iflearner-flow-client
```
Then you can reference the `flow_federate_sdk` library for interface calls

## Initialization

We need to initialize the operation first, mainly to complete the relevant parameters of configuring the connection service, and generate a client object.

**Parameters**

| parameter |required | type | description |
| :------------- | :--- | :----- | --------------------- ---------------------------------------- |
| host | yes | string | The host for connecting `iflearner_flow_federate` server |
| port| yes | string | The port for connecting `iflearner_flow_federate` server |

**Usage**
```shell
from flow_federate_sdk import FlowFederateSdk
# use real ip address to initialize SDK
flow_federate_client = FlowFederateSdk(host="127.0.0.1", port="1235")
```

--8<--
client/sdk/flow_federate/task.md
--8<--