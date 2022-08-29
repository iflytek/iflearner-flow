## Task

### Create
创建任务

**Function**
```bash
create(
        cls,
        name: str,
        template_id: str,
        remark: str,
        federate_data: List[Any],
    ) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| name | yes | string | 任务名称 |
| template_id | yes | string | 任务关联的模板id |
| remark | no | string | 任务备注信息 |
| federate_data | yes | array | 任务关联的联邦方信息 |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |
| data.task_id | string | 创建的任务id |

**Call Example**
```bash
flow_server_client.task.create(
    name="testCase1", 
    template_id="ea0f10bfbaf64a74a061d54c94cc69", 
    remark="This is a remark.", 
    federate_data=[{"federated_id": "federate-1", "federated_data": ""}],
)
```

**Return Example**
```json
{
    "data": {
        "task_id": "b1731d312dae4edba6d07a6fff547b4a"
    },
    "ret_code": 0,
    "ret_msg": "success"
}
```


### Update
更新任务

**Function**
```bash
update(cls,
        task_id: str,
        name: str,
        template_id: str,
        remark: str,
        federate_data: List,
    ) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | 任务id |
| name | yes | string | 任务名称 |
| template_id | yes | string | 任务关联的模板id |
| remark | no | string | 任务备注信息 |
| federate_data | yes | array | 任务关联的联邦方信息 |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |

**Call Example**
```bash
flow_server_client.task.update(
    task_id="0578abed1032425499abd20f2ef67938", 
    name="testCase", 
    template_id="ea0f10bfbaf64a74a061d54c94cc69", 
    remark="This is a remark.", 
    federate_data=[{"federated_id": "federate-1", "federated_data": "aa"}],
)
```

**Return Example**
```json
{
    "ret_code": 0,
    "ret_msg": "success"
}
```


### Get
获取任务详情

**Function**
```bash
get(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | 任务id |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |
| data | dict | 任务详情 |

**Call Example**
```bash
flow_server_client.task.get("0578abed1032425499abd20f2ef67938")
```

**Return Example**
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


### List
获取任务列表

**Function**
```bash
list(cls, page: int, limit: int) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| page | yes | int | 页码 |
| limit | yes | int | 每页的数量 |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |
| data.task_count | int | 任务总数 |
| data.tasks | array | 任务列表 |

**Call Example**
```bash
flow_server_client.task.list(1, 10)
```

**Return Example**
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


### Delete
删除任务

**Function**
```bash
delete(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | 任务id |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |

**Call Example**
```bash
flow_server_client.task.delete("5986dd8986654fa6af3404a1d1eada72")
```

**Return Example**
```json
{
    "ret_code": 0,
    "ret_msg": "success"
}
```


### Start
开始任务

**Function**
```bash
start(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | 任务id |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |

**Call Example**
```bash
flow_server_client.task.start("5986dd8986654fa6af3404a1d1eada72")
```

**Return Example**
```json
{
    "ret_code": 0,
    "ret_msg": "success"
}
```


### Stop
停止任务

**Function**
```bash
stop(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | 任务id |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |

**Call Example**
```bash
flow_server_client.task.stop("5986dd8986654fa6af3404a1d1eada72")
```

**Return Example**
```json
{
    "ret_code": 0,
    "ret_msg": "success"
}
```
