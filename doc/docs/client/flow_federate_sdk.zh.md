## Introduction

我们将介绍如何使用`flow_federate_sdk`sdk库与`iflearner_flow_federate`服务进行交互。

## Installation
您可以执行下述命令进行快速安装:
```shell
pip install iflearner-flow-client
```
然后, 您就可以引用`flow_federate_sdk`库进行接口调用

## Initialization

我们需要先初始化操作，主要是完成配置连接服务的相关参数, 生成一个client对象。

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| host | yes | string | The host for connecting `iflearner_flow_federate` server |
| port| yes | string | The port for connecting `iflearner_flow_federate` server |

**Usage**
```shell
from flow_federate_sdk import FlowFederateSdk
# use real ip address to initialize SDK
flow_federate_client = FlowFederateSdk(host="127.0.0.1", port="1235")
```

--8<--
client/sdk/flow_federate/task.zh.md
--8<--