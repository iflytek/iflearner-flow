## Introduction

First, You can execute the following command to quickly install:
```shell
pip install iflearner-flow-client
```

Second, We will introduce how to interact with `iflearner_flow_federate` using the command line tool`flow_federate_cli`, the following are
the subcommands.
```shell
Usage: flow_federate_cli [OPTIONS] COMMAND [ARGS]...

  Iflearner Flow Federate  Cli.

Options:
  -h, --help  Show this message and exit.

Commands:
  init  Iflearner Federate Flow Cli Init Command
  task  Task Operations Group
```

The specific command usage is as follows.


## Initialization

Before using the command line, we need to initialize the operation, mainly to configure the relevant parameters of the connection service

**Usage**
```shell
flow_federate_cli init [OPTIONS]
```

**OPTIONS**

| parameter name |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| --host | yes | string | The host of the connection server`iflearner_flow_federate`  |
| --port | yes | string | The port of the connection server`iflearner_flow_federate` |

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
client/cli/flow_federate/task.md
--8<--