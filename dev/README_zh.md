# 开发指南
本文档主要用于开发阶段的规范脚本、一些工具脚本的指南。

## 代码规范化
采用一些代码规范化规整和检测工具，检测代码规范并按照提示进行调整，主要步骤为:

1. 自动格式化     
采用isort、black、docformatter工具对指定代码自动调整规范，执行命令如下所示:
    ```shell
    bash format.sh
    ```

2. 测试规范化     
采用isort、black、docformatter、mypy、flake8工具对指定代码进行规范化测试，执行命令如下所示:
    ```shell
    bash test.sh
    ```
    > 请按照相应的提示进行整改。

## 导出swagger
自动导出`flask API`的rest接口schema文件，并自动同步到doc目录用于API文档生成。

执行命令如下所示:
```shell
bash export_swagger.sh
```

## 导出错误码
自动导出`iflearner-flow`代码中定义的错误码，并自动同步到doc目录中用于API文档生成。

执行命令如下所示:
```shell
bash export_errcode_md.sh
```