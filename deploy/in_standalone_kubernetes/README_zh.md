## 真实场景下的部署

`iflearner-flow`, 分为两类角色(`flow-server`，`flow-federate`), 其中:
- `flow-server`是中心端，主要用于模型聚合和各方流程控制
- `flow-federate`是联邦端，是具体的联邦任务方，主要进行实际的联邦任务训练。

涉及到的`iflearner_flow_server`是实现`flow_server`角色的组件，`iflearner_flow_federate`是实现`flow_federate`角色的组件.
其中:
- `iflearner_flow_server`是中心端，**只需要部署一套**
- `iflearner_flow_federate`**需要在每个联邦方进行独立的部署一套**。

### 前置条件
- 安装kubernetes>=1.18
- 安装iflearner-operator

详细资料参阅: [在线安装部署](https://iflytek.github.io/iflearner-flow/zh/installation/online_on_kubernetes_installation/)

### 部署iflearner_flow_server
参阅: [iflearner_flow_server](iflearner_flow_server/README_zh.md)

### 部署iflearner_flow_federate
参阅: [iflearner_flow_federate](iflearner_flow_federate/README_zh.md)