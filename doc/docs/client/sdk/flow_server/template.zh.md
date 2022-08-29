## Template

### create
创建一个任务模板

**Function**
```bash
create(
        cls,
        name: str,
        image_url: str,
        workdir: str,
        command: List[str],
        remark: str = None,
        hyper_parameter: list = None,
    ) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| name | yes | string | 模板名称 |
| image_url| yes | string | 镜像url地址 |
| workdir | yes | string | 镜像工作目录 |
| command  | yes | array | 镜像启动命令 |
| remark | no | string | 模板备注信息 |
| hyper_parameter | no | array | 镜像启动的超参数 |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |
| data.template_id | string | 创建的模板id |

**Call Example**
```bash
flow_server_client.template.create(
            name="template_01",
            image_url="iflearner_ocr:0.0.1",
            workdir="/data/ocr/script",
            command=[],
            remark="",
            hyper_parameter = [],
        )
```

**Return Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success",
  "data": {
    "template_id": "20f42769b99b492691da1ba2f236b1"
  }
}
```

### update
更新一个指定的任务模板。

**Function**
```bash
update(
        cls,
        template_id: str,
        name: str,
        image_url: str,
        workdir: str,
        command: List[str],
        remark: str = None,
        hyper_parameter: list = None,
    ) -> Dict[str, Any]
```

**Parameters**

| 参数 |必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| template_id | yes | string | 模板id |
| name | yes | string | 模板名 |
| image_url| yes | string | 镜像url地址 |
| workdir | yes | string | 镜像工作目录 |
| command  | yes | array | 镜像启动命令 |
| remark | no | string | 模板描述 |
| hyper_parameter | no | array | 镜像启动超参数 |

**Return**    

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |

**Call Example**
```bash
flow_server_client.template.update(
            template_id="20f42769b99b492691da1ba2f236b1",
            name="template_01",
            image_url="iflearner_ocr:0.0.2",
            workdir="/data/ocr/script",
            command=[],
        )
```

**Return Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```

### get
查询一个指定的任务模板

**Function**
```bash
get(cls, template_id: str) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| template_id | yes | string | 模板id |

**Return**

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ----------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |
| data.name | string | 模板名称 |
| data.remark | string | 模板备注信息 |
| data.image_url | string | 镜像的url地址
| data.workdir | string | 镜像的工作目录 |
| data.command | array | 镜像的启动命令 |
| data.hyper_parameter | array | 镜像的启动超参数 |
| data.template_id | string | 模板id |
| data.create_time | string | 模板创建时间 |
| data.modify_time | string | 模板更新时间 |


**Call Example**
```bash
flow_server_client.template.get(
            template_id="20f42769b99b492691da1ba2f236b1"
        )
```

**Return Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success",
  "data": {
    "name": "template_003",
    "remark": "template test",
    "image_url": "pytorch_ocr:latest",
    "workdir": "/data/ocr",
    "command": [
      "python",
      "run.py"
    ],
    "hyper_parameter": [
      "epoch=1"
    ],
    "template_id": "20f42769b99b492691da1ba2f236b1",  
    "create_time": "Mon, 25 Jul 2022 15:59:55 -0000",
    "modify_time": "Mon, 25 Jul 2022 15:59:55 -0000"
  }
}
```


### list
批量查询模板信息

**Function**
```bash
list(cls, keyword: str = "", page: int = 1, limit: int = 10) -> Dict[str, Any]
```

**Parameters**

| 参数 | 必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| page | no | int | 当前页 |
| limit | no | int | 当前页查询数目 |

**Return**

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | --------------------------------------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |
| data.templates[index].name | string | 模板名 |
| data.templates[index].remark | string | 模板备注信息 |
| data.templates[index].image_url | string | 镜像的url地址
| data.templates[index].workdir | string | 镜像的工作目录 |
| data.templates[index].command | array | 镜像的启动命令 |
| data.templates[index].hyper_parameter | array | 镜像启动的超参数 |
| data.templates[index].template_id | string | 模板id |
| data.templates[index].create_time | string | 模板创建时间 |
| data.templates[index].modify_time | string | 模板更新时间 |


**Call Example**
```bash
flow_server_client.template.list(keyword="", page=1, limit=10)
```

**Return Example**
```json
  "ret_code": 0,
  "ret_msg": "success",
  "data": {
    "templates": [
      {
        "name": "f5b75371-5dc0-47c6-9a8d-86cd3e06b56a",
        "remark": "",
        "image_url": "iflearner_ocr:0.0.1",
        "workdir": "/data/ocr/script",
        "command": [],
        "hyper_parameter": null,
        "template_id": "0381e7b3bedb4578a3b5a8d11cd65d",
        "create_time": "Wed, 20 Jul 2022 16:39:19 -0000",
        "modify_time": "Wed, 20 Jul 2022 16:39:19 -0000"
      },
      {
        "name": "707fc798-774a-44be-9844-019c4a7e6714",
        "remark": "",
        "image_url": "iflearner_ocr:0.0.1",
        "workdir": "/data/ocr/script",
        "command": [],
        "hyper_parameter": null,
        "template_id": "0596cb767f0448f4b4fa4f11f65fa8",
        "create_time": "Wed, 20 Jul 2022 17:06:20 -0000",
        "modify_time": "Wed, 20 Jul 2022 17:06:20 -0000"
      }
    ],
    "template_count": 108
  }
}
```

### delete
删除一个指定的模板

**Function**
```bash
delete(cls, template_id: str) -> Dict[str, Any]:
```

**Parameters**

| 参数 |必填 | 类型 | 说明 |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| template_id | yes | string | 模板id |

**Return**

| 参数 | 类型 | 说明 |
| :-------------------------------------------- | :----- | ----------------------------------------- |
| ret_code | int | 结果码 |
| ret_msg | string | 结果描述信息 |


**Call Example**~~~~
```bash
flow_server_client.template.delete(
            template_id=self._generate_template_id
        )
```

**Return Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```
