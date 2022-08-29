# 环境构建和运行
该文档将指导如何构建该服务的docker镜像以及在kubernetes上启动。

## 在kubernetes上部署
1. 预置条件: 完成镜像的构建。请参阅: [docker环境下构建](../docker/README_zh.md) 
2. 修改: 你需要修改`iflearner_flow_federate.yaml`文件，修改对应挂载的配置文件、日志目录和镜像等
3. 执行: 拷贝镜像和`iflearner_flow_federate.yaml`文件到kubernetes集群上，执行下述命令即可:
```shell
kubectl apply -f iflearner_flow_federate.yaml
```