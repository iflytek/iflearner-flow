## Introduction

首先，我们将通过下述命令快速安装:
```shell
pip install iflearner-flow-client
```

接下来, 我们将介绍如何使用命令行工具`flow_federate_cli`与`iflearner_flow_federate`进行交互，以下是子命令。
```shell
Usage: flow_federate_cli [OPTIONS] COMMAND [ARGS]...

  Iflearner Flow Federate  Cli.

Options:
  -h, --help  Show this message and exit.

Commands:
  init  Iflearner Federate Flow Cli Init Command
  task  Task Operations Group
```

具体命令用法如下。

## Initialization

在使用命令行之前，我们需要初始化操作，主要是配置连接服务的相关参数

**Usage**
```shell
flow_federate_cli init [OPTIONS]
```

**OPTIONS**

|参数名称 |必填 |类型 |描述 |
| :---------------- | :--- | :----- | -------------------------------------------------------------- |
| --host | 是 | string | 连接`iflearner_flow_federate`的ip地址  |
| --port | 是 | string | 连接`iflearner_flow_federate`的端口 |

**Request Example**

```shell
flow_federate_cli init --host 127.0.0.1 --port 1235
```

**Request Example**
```json
{
  "ret_code": 0,
  "ret_message": "success"
}
```

--8<--
client/cli/flow_federate/task.zh.md
--8<--