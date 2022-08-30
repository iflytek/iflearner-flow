# 在kubernetes集群上搭建iflearner-flow

## 1. 总体介绍
### 1.1 系统介绍
Iflearner Flow是一个基于底层联邦学习框架Iflearner，针对横向联邦学习场景建模的多方联合任务安全调度平台。

### 1.2 组件说明
1. 服务端方

    | 组件           |版本           |  说明                                   |
    | -------------- | --------- | -------------------------------------- |
    | kubernetes          | 1.18      | 容器编排集群，flow-server依赖 |
    | mysql          | 8.0      | 数据存储，flow-server依赖 |
    | ifleaner-flow-server          | 1.0.0     | server侧调度组件 |
    | ifleaner-operator          | 0.0.1     | kubernetes crd的控制器 |

2. 联邦方

    | 组件           |版本           |  说明                                   |
    | -------------- | --------- | -------------------------------------- |
    | kubernetes          | 1.18      | 容器编排集群，flow-server依赖 |
    | mysql          | 8.0      | 数据存储，flow-server依赖 |
    | ifleaner-flow-federate          | 1.0.0     | federate侧调度组件 |
    | ifleaner-operator          | 0.0.1     | kubernetes crd的控制器 |

### 1.3 系统设计

[系统设计](../tutorial/system_arch_zh.md)

## 2. 详细设计
### 2.1 部署规划
 本示例为了便于演示，服务侧和联邦侧都只有一台主机，事实上依托于kubernetes，可以自由扩大每侧的集群规模。

1. 服务侧

    | IP地址                | 操作系统                | 主机配置 | 存储 | 部署模块                                                     |
    | --------------------- | ----------------------- | -------- | ---- | -------------------------------- |
    | 172.31.0.1 | CentOS 7.4 | 16C32G    | 200G | kubernetes、mysql、iflearner-flow-server、ifleaner-operator |

2. 联邦侧

    | 联邦              | IP地址                | 操作系统                | 主机配置 | 存储 | 部署模块                                                     |
    | --------------------- | --------------------- | ----------------------- | -------- | ---- | -------------------------------- |
    | 联邦1 | 172.31.0.2 | CentOS 7.4 | 16C32G, GPU卡一张(非必须)    | 200G | kubernetes、mysql、iflearner-flow-server、ifleaner-operator |
    | 联邦2 | 172.31.0.3  | CentOS 7.4 | 16C32G, GPU卡一张(非必须)    | 200G | kubernetes、mysql、iflearner-flow-federate、ifleaner-operator |
    > 这里只演示了只有两个联邦的场景，可以自由扩充

### 2.2 主机资源和操作系统要求
| **类别** | **说明**                                                     |
| -------- | ------------------------------------------------------------ |
| 主机配置 | 不低于16C、32G、200G，千兆网卡、最好配置GPU卡进行训练加速                                    |
| 操作系统 | CentOS linux 7.4及以上                 |
| 文件系统 | 1、持久化数据盘默认挂载在/data目录下。<br/> 2、根目录空闲空间不低于20G。 |
| 系统参数 | 1、文件句柄数不低于65535。<br> 2、用户进程数不低于65535。     |

### 2.3 网络要求
| 类别         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| 防火墙策略   | 1、防火墙设备需要支持长连接和需要对连接数无限制。 |

## 3. 项目部署
### 3.1 部署示意图

### 3.2 服务侧部署
#### 3.2.1 部署kubernetes
推荐一个极简的一键部署方式[sealos](https://www.sealos.io/zh-Hans/docs/Intro)
> 当前支持版本为1.18

#### 3.2.2 部署iflearner-operator
参见[iflearner-operator](https://github.com/iflytek/iflearner-operator)文档

#### 3.2.3 部署iflearner-flow-server
可以通过下述命令快速完成部署:

```shell
kubectl create -f python/iflearner_flow_server/deployment.yaml
```

### 3.3 联邦侧部署
每个联邦方执行步骤一致，下述为单个联邦方下的执行步骤

#### 3.3.1 部署kubernetes
推荐一个极简的一键部署方式[sealos](https://www.sealos.io/zh-Hans/docs/Intro)
> 当前支持版本为1.18

#### 3.3.2 部署iflearner-operator
参见[iflearner-operator](https://github.com/iflytek/iflearner-operator)文档

#### 3.3.3 部署iflearner-flow-federate
可以通过下述命令快速完成部署:

```shell
kubectl create -f python/iflearner_flow_federate/deployment.yaml
```

## 4. 系统运维
### 4.1 查看组件状态

```shell
kubectl get pods -o wide -n iflearner
```

### 4.2 查看组件日志

```shell
kubectl logs *** -n iflearner
```

### 4.3 查看组件持久化文件目录

```shell
kubectl describe pods *** -n iflearner
```

## 5. 系统卸载
### 5.1 卸载iflearner-flow-server
可以通过下述命令快速完成卸载:

```shell
kubectl delete -f python/iflearner_flow_server/deployment.yaml
```

### 5.2 卸载iflearner-flow-federate
可以通过下述命令快速完成卸载:

```shell
kubectl delete -f python/iflearner_flow_federate/deployment.yaml
```

### 5.3 卸载iflearner-operator
参见[iflearner-operator](https://github.com/iflytek/iflearner-operator)文档

