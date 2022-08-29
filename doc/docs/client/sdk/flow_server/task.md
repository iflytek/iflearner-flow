## Task

### Create
create task

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

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| name | yes | string | the name of task |
| template_id | yes | string | task-related template |
| remark | no | string | task remark |
| federate_data | yes | array | task-related federate |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data.task_id | string | task id |

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
update task

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

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | task id |
| name | yes | string | the name of task |
| template_id | yes | string | task-related template |
| remark | no | string | task remark |
| federate_data | yes | array | task-related federate |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |

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
get task detail

**Function**
```bash
get(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | task id |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data | dict | task detail |

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
get task list

**Function**
```bash
list(cls, page: int, limit: int) -> Dict[str, Any]
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| page | yes | int | page index |
| limit | yes | int | page size |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data.task_count | int | total task number |
| data.tasks | array | task list |

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
delete task

**Function**
```bash
delete(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | task id |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |

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
start task

**Function**
```bash
start(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | task id |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |

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
stop task

**Function**
```bash
stop(cls, task_id: str) -> Dict[str, Any]
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| task_id | yes | string | task id |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |

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
