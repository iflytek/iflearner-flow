## 部署指南

当前，iflearner-flow基于kubernetes，支持大规模集群上的联邦学习任务调度。

当前部署方式, 主要支持:
- 真实场景下的部署(每方都有一套独立的kubernetes集群)
- 验证测试场景下的部署(各方共享一套kubernetes集群)

### 真实场景下的部署
参考: [in_standalone_kubernetes](in_standalone_kubernetes/README_zh.md)

### 验证测试场景下的部署
参考: [all_in_one_kubernetes](all_in_one_kubernetes/README_zh.md)