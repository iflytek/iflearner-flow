## Template

### create
Create a task template.

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

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| name | yes | string | Template name |
| image_url| yes | string | Image url address of template configuration |
| workdir | yes | string | Image workdir |
| command  | yes | array | Image startup command |
| remark | no | string | Template description |
| hyper_parameter | no | array | Hyper parameter passed by image startup |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data.template_id | string | Generated template id |

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
Update a specified template.

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

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| template_id | yes | string | The id of template |
| name | yes | string | Template name |
| image_url| yes | string | Image url address of template configuration |
| workdir | yes | string | Image workdir |
| command  | yes | array | Image startup command |
| remark | no | string | Template description |
| hyper_parameter | no | array | Hyper parameter passed by image startup |

**Return**    

| parameter | type | description |
| :-------------------------------------------- | :----- | ------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |

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
Query a specified template.

**Function**
```bash
get(cls, template_id: str) -> Dict[str, Any]
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| template_id | yes | string | The id of template |

**Return**

| parameter | type | description |
| :-------------------------------------------- | :----- | ----------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data.name | string | Template name |
| data.remark | string | Template remark |
| data.image_url | string | The url address of the template image
| data.workdir | string | The working directory of the template image |
| data.command | array | Image startup command |
| data.hyper_parameter | array | Hyperparameters for mirror startup |
| data.template_id | string | Unique ID of the template |
| data.create_time | string | Template creation time |
| data.modify_time | string | Template update time |


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
Batch query template information

**Function**
```bash
list(cls, keyword: str = "", page: int = 1, limit: int = 10) -> Dict[str, Any]
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| page | no | int | The current page |
| limit | no | int | The query num of current page |

**Return**

| parameter | type | description |
| :-------------------------------------------- | :----- | --------------------------------------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |
| data.templates[index].name | string | Template name |
| data.templates[index].remark | string | Template remarks |
| data.templates[index].image_url | string | URL of template image
| data.templates[index].workdir | string | The working directory of the template image |
| data.templates[index].command | array | Image startup command |
| data.templates[index].hyper_parameter | array | Hyperparameters for mirror startup |
| data.templates[index].template_id | string | Unique ID of the template |
| data.templates[index].create_time | string | Template creation time |
| data.templates[index].modify_time | string | Template update time |


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
Delete a specified template.

**Function**
```bash
delete(cls, template_id: str) -> Dict[str, Any]:
```

**Parameters**

| parameter |required | type | description |
| :-------------- | :--- | :----- | ------------------------------------------------------------- |
| template_id | yes | string | The id of template |

**Return**

| parameter | type | description |
| :-------------------------------------------- | :----- | ----------------------------------------- |
| ret_code | int | Return code |
| ret_msg | string | Return information |


**Call Example**
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
