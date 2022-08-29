## Task

### create

创建任务

**Usage**
```bash
flow_server_cli task create [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| -n, --task_name | 是 | string | 任务名称 |
| -t, --template_id | 是 | string | 任务关联的模板 |
| -r, --remark | 否 | string | 任务备注 |
| -fd, --federate_data | 是 | array | 任务关联的联邦方信息 |

**Response**    

| 参数名                          | 类型   | 说明                                                                  |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |
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

更新任务

**Usage**
```bash
flow_server_cli task update [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | 是 | string | 任务id |
| -n, --task_name | 是 | string | 任务名称 |
| -t, --template_id | 是 | string | 任务关联模板 |
| -r, --remark | 否 | string | 任务备注 |
| -fd, --federate_data | 是 | array | 任务关联的联邦方信息 |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :-------------------------------------------- | :----- | ------------------------------------ |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |

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

获取任务详情

**Usage**
```bash
flow_server_cli task get [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | 是 | string | 任务id |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :-------------------------------------------- | :----- | ----------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |
| data | dict | 任务详情 |

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

获取任务列表

**Usage**
```bash
flow_server_cli task list [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
| -p, --page   | 否   | int | 当前页，默认为1  |
| -l, --limit   | 否   | int | 当前页查询的数目，默认为10  |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :-------------------------------------------- | :----- | --------------------------------------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |
| data.task_count | int | 任务总数 |
| data.tasks | array | 当前页的任务列表 |

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

删除任务

**Usage**
```bash
flow_server_cli task delete [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | 是 | string | 任务id |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :-------------------------------------------- | :----- | ------------------------ |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |

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

开始任务

**Usage**
```bash
flow_server_cli task start [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | 是 | string | 任务id |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :-------------------------------------------- | :----- | ------------------------ |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |

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

停止任务

**Usage**
```bash
flow_server_cli task stop [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
| -id, --task_id | 是 | string | 任务id |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :-------------------------------------------- | :----- | ------------------------ |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |

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
