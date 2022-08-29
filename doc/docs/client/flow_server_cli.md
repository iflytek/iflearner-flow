## Introduction

First, You can execute the following command to quickly install:
```shell
pip install iflearner-flow-client
```

Secondly, We will introduce how to interact with `iflearner_flow_server` using the command line tool`flow_server_cli`, the following are
the subcommands.
```shell
Usage: flow_server_cli [OPTIONS] COMMAND [ARGS]...

  Iflearner Flow Server  Cli.

Options:
  -h, --help  Show this message and exit.

Commands:
  init      Iflearner Server Flow Cli Init Command
  task      Task Operations Group
  template  Template Operations Group
```

The specific command usage is as follows.


## Initialization

Before using the command line, we need to initialize the operation, mainly to configure the relevant parameters of the connection service

**Usage**
```shell
flow_server_cli init [OPTIONS]
```

**OPTIONS**

| parameter name |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| --host | yes | string | The host of the connection server`iflearner_flow_server`  |
| --port | yes | string | The port of the connection server`iflearner_flow_server` |

**Request Example**

```shell
flow_server_cli init --host 127.0.0.1 --port 1235
```

**Request Example**
```json
{
  "ret_code": 0,
  "ret_message": "success"
}
```

--8<--
client/cli/flow_server/template.md
client/cli/flow_server/task.md
--8<--