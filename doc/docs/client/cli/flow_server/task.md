## Task

### create

Create task

**Usage**
```bash
flow_server_cli task create [OPTIONS]
```

**OPTIONS**

| parameter name |rRequired | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| -n, --task_name | yes | string | the name of task |
| -t, --template_id | yes | string | task-related template |
| -r, --remark | no | string | task remark |
| -fd, --federate_data | yes | array | task-related federate |

**Response**    

| parameter name | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data.task_id | string | task id |

**Request Example**

```bash
flow_server_cli task create -n task01 -t ea0f10bfbaf64a74a061d54c94cc69 -r "This is a remark." -fd '[{"federated_id": "federate-1", "federated_data": ""}]'
```

**Response Example**
```json
{
    "data": {
        "task_id": "b1731d312dae4edba6d07a6fff547b4a"
    },
    "ret_code": 0,
    "ret_msg": "success"
}
```


### update

Update task

**Usage**
```bash
flow_server_cli task update [OPTIONS]
```

**OPTIONS**

| parameter Name | required | type | description |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | yes | string | task id |
| -n, --task_name | yes | string | the name of task |
| -t, --template_id | yes | string | task-related template |
| -r, --remark | no | string | task remark |
| -fd, --federate_data | yes | array | task-related federate |

**Response**

| parameter name | type | description |
| :-------------------------------------------- | :----- | ------------------------------------ |
| ret_code | int | Return code |
| ret_msg | string | Return information |

**Request Example**
```bash
flow_server_cli task update -id bbc0c30e96bc4da29b2b326fb1f8786e -n task01 -t ea0f10bfbaf64a74a061d54c94cc69 -r "This is a new remark." -fd '[{"federated_id": "federate-1", "federated_data": ""}]'
```

**Response Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```


### get

Get task

**Usage**
```bash
flow_server_cli task get [OPTIONS]
```

**OPTIONS**

| parameter Name | required | type | description |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | yes | string | task id |

**Response**

| parameter name | type | description |
| :-------------------------------------------- | :----- | ----------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data | dict | task detail |

**Request Example**
```bash
flow_server_cli task get -id bbc0c30e96bc4da29b2b326fb1f8786e
```

**Response Example**
```json
{
    "data": {
        "create_time": "Mon, 25 Jul 2022 20:31:21 -0000",
        "federate_data": [
            {
                "federated_data": "aa",
                "federated_id": "federate-1"
            }
        ],
        "modify_time": "Mon, 25 Jul 2022 20:31:21 -0000",
        "name": "testCase",
        "party_status": null,
        "remark": "This is a remark.",
        "status": null,
        "task_id": "0578abed1032425499abd20f2ef67938",
        "template_id": "ea0f10bfbaf64a74a061d54c94cc69"
    },
    "ret_code": 0,
    "ret_msg": "success"
}
```

### list

Get task list

**Usage**
```bash
flow_server_cli task list [OPTIONS]
```

**OPTIONS**

| parameter Name | required | type | description |
| :-------------- | :--- | :----- | -------------- |
| -p, --page | no | int | Current page, default is 1 |
| -l, --limit | no | int | The number of queries on the current page, default is 10 |

**Response**

| parameter name | type | description |
| :-------------------------------------------- | :----- | --------------------------------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data.task_count | int | total task number |
| data.tasks | array | task list |

**Request Example**
```bash
flow_server_cli task list -p 1 -l 10
```

**Response Example**
```json
{
    "data": {
        "task_count": 1,
        "tasks": [
            {
                "create_time": "Tue, 26 Jul 2022 16:05:59 -0000",
                "federate_data": [
                    {
                        "federated_data": "",
                        "federated_id": "federate-1"
                    }
                ],
                "modify_time": "Tue, 26 Jul 2022 16:05:59 -0000",
                "name": "testCase1",
                "party_status": null,
                "remark": "This is a remark.",
                "status": null,
                "task_id": "b1731d312dae4edba6d07a6fff547b4a",
                "template_id": "ea0f10bfbaf64a74a061d54c94cc69"
            }
        ]
    },
    "ret_code": 0,
    "ret_msg": "success"
}
```


### delete

Delete task

**Usage**
```bash
flow_server_cli task delete [OPTIONS]
```

**OPTIONS**

| parameter Name | required | type | description |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | yes | string | task id |

**Response**

| parameter name | type | description |
| :-------------------------------------------- | :----- | ------------------------ |
| ret_code | int | Return code |
| ret_msg | string | Return information |

**Request Example**
```bash
flow_server_cli task delete -id 20f42769b99b492691da1ba2f236b1
```

**Response Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```


### start

Start task

**Usage**
```bash
flow_server_cli task start [OPTIONS]
```

**OPTIONS**

| parameter Name | required | type | description |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | yes | string | task id |

**Response**

| parameter name | type | description |
| :-------------------------------------------- | :----- | ------------------------ |
| ret_code | int | Return code |
| ret_msg | string | Return information |

**Request Example**
```bash
flow_server_cli task start -id 20f42769b99b492691da1ba2f236b1
```

**Response Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```


### stop

Stop task

**Usage**
```bash
flow_server_cli task stop [OPTIONS]
```

**OPTIONS**

| parameter Name | required | type | description |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | yes | string | task id |

**Response**

| parameter name | type | description |
| :-------------------------------------------- | :----- | ------------------------ |
| ret_code | int | Return code |
| ret_msg | string | Return information |

**Request Example**
```bash
flow_server_cli task stop -id 20f42769b99b492691da1ba2f236b1
```

**Response Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```
