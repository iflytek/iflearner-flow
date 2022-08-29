## Template

### create

创建一个任务模板

**Usage**
```bash
flow_server_cli template create [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
|  -n, --template_name  | 是   | string | 模板名称  |
| -r, --remark | 否   | string | 模板说明 |
| -i, --image_url| 是   | string | 模板配置的镜像url地址 |
|  -w, --workdir | 否   | string | 镜像workdir |
| -c, --command | 否   | string | 镜像启动命令 |
| -hp, --hyper_parameter  | 否   | string | 镜像启动传递的超参 |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :------------------------------ | :----- | --------------------------------------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |
| data.template_id                          | string | 生成的模板id                                                              |

**Request Example**
```bash
flow_server_cli template create -n template_01 -r 'template test' -i pytorch_ocr:latest -w /data/ocr -c '["python", "run.py"]' -hp '["epoch=1"]'
```

**Response Example**
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

更新一个任务模板

**Usage**
```bash
flow_server_cli template update [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
|  -id, --template_id  | 是   | string | 模板的唯一标识  |
|  -n, --template_name  | 是   | string | 模板名称  |
| -r, --remark | 否   | string | 模板说明 |
| -i, --image_url| 是   | string | 模板配置的镜像url地址 |
|  -w, --workdir | 否   | string | 镜像workdir |
| -c, --command | 否   | string | 镜像启动命令 |
| -hp, --hyper_parameter  | 否   | array | 镜像启动传递的超参 |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :------------------------------ | :----- | --------------------------------------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |
| data.template_id                          | string | 生成的模板id                                                              |

**Request Example**
```bash
flow_server_cli template update -id 20f42769b99b492691da1ba2f236b1 -n template_01 -r 'template test' -i pytorch_ocr:latest -w /data/ocr -c '["python", "run.py"]' -hp '["epoch=1"]'
```

**Response Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```

### get

查询一个任务模板信息

**Usage**
```bash
flow_server_cli template get [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
|  -id, --template_id  | 是   | string | 模板的唯一标识  |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :------------------------------ | :----- | --------------------------------------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |
| data.name                          | string | 模板名称                                                              |
| data.remark                          | string | 模板备注                                                              |
| data.image_url                          | string | 模板镜像的url地址  
| data.workdir                          | string | 模板镜像的工作目录 |
| data.command                          | array | 镜像启动命令                                                              |
| data.hyper_parameter                          | array |  镜像启动的超参                                                             |
| data.template_id                          | string |  模板的唯一标识                                                             |
| data.create_time                          | string |  模板的创建时间                                                             |
| data.modify_time                          | string |  模板的更新时间                                                             |

**Request Example**
```bash
flow_server_cli template get -id 20f42769b99b492691da1ba2f236b1
```

**Response Example**
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

**Usage**
```bash
flow_server_cli template list [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
| -p, --page   | 否   | int | 当前页，默认为1  |
| -l, --limit   | 否   | int | 当前页查询的数目，默认为10  |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :------------------------------ | :----- | --------------------------------------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |
| data.templates[index].name                          | string | 模板名称                                                              |
| data.templates[index].remark                          | string | 模板备注                                                              |
| data.templates[index].image_url                          | string | 模板镜像的url地址  
| data.templates[index].workdir                          | string | 模板镜像的工作目录 |
| data.templates[index].command                          | array | 镜像启动命令                                                              |
| data.templates[index].hyper_parameter                          | array |  镜像启动的超参                                                             |
| data.templates[index].template_id                          | string |  模板的唯一标识                                                             |
| data.templates[index].create_time                          | string |  模板的创建时间                                                             |
| data.templates[index].modify_time                          | string |  模板的更新时间                                                             |

**Request Example**
```bash
flow_server_cli template list -p 1 -l 2
```

**Rexponse Example**
```json
{
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

删除一个指定的任务模板

**Usage**
```bash
flow_server_cli template delete [OPTIONS]
```

**OPTIONS**

| 参数名          | 必选 | 类型   | 说明           |
| :-------------- | :--- | :----- | -------------- |
|  -id, --template_id  | 是   | string | 模板的唯一标识  |

**Response**

| 参数名                          | 类型   | 说明                                                                  |
| :------------------------------ | :----- | --------------------------------------------------------------------- |
| ret_code                         | int    | 返回码                                                                |
| ret_msg                          | string | 返回信息                                                              |

**Request Example**
```bash
flow_server_cli template delete -id 20f42769b99b492691da1ba2f236b1
```

**Response Example**
```json
{
  "ret_code": 0,
  "ret_msg": "success"
}
```