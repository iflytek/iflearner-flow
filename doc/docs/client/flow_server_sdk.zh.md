## Introduction

我们将介绍如何使用`flow_server`sdk与`iflearner_flow_server`进行交互。

## Initialization

我们需要先初始化操作，主要是完成配置连接服务的相关参数, 生成一个client对象。

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| host | yes | string | The host for connecting `iflearner_flow_server` server |
| port| yes | string | The port for connecting `iflearner_flow_server` server |

**Usage**
```shell
from flow_server_sdk import FlowServerSdk
# use real ip address to initialize SDK
flow_server_client = FlowServerSdk(host="127.0.0.1", port="1235")
```

--8<--
client/sdk/flow_server/template.zh.md
client/sdk/flow_server/task.zh.md
--8<--