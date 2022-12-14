# Deploy iflearner-flow on the kubernetes cluster

## 1. General introduction
### 1.1 System introduction
Iflearner Flow is a multi-party joint task security scheduling platform based on the underlying federated learning framework Iflearner, which models horizontal federated learning scenarios.

### 1.2 Component Description
1. Server side

    | Component | Version | Description |
    | -------------- | --------- | -------------------------------------- |
    | kubernetes | 1.18 | Container orchestration cluster, flow-server dependency |
    | mysql | 5.7 | data storage, flow-server dependency |
    | ifleaner-flow-server | 0.1.0 | server-side scheduling component |
    | ifleaner-operator          | 0.0.1     | kubernetes crd contorller |

2. Federate side

    | Component | Version | Description |
    | -------------- | --------- | -------------------------------------- |
    | kubernetes | 1.18 | Container orchestration cluster, flow-server dependency |
    | mysql | 5.7 | data storage, flow-server dependency |
    | ifleaner-flow-federate | 0.1.0 | federate-side scheduling component |
    | ifleaner-operator          | 0.0.1     | kubernetes crd contorller |

### 1.3 System Design

[Iflearner Flow Design](../tutorial/system_arch.md)

## 2. Detailed design
### 2.1 Deployment Planning
In this example, for the convenience of demonstration, there is only one host on the service side, and the federation side. In fact, relying on kubernetes, the cluster size on each side can be freely expanded.

1. Service side

    | IP Address | Operating System | Host Configuration | Storage | Deployment Modules |
    | --------------------- | ----------------------- | -------- | ---- | -------------------------------- |
    | 172.31.0.1 | CentOS 7.4 | 16C32G | 100G | kubernetes, mysql, iflearner-flow-server |

2. Federal side

    | Federation | IP Addresses | Operating Systems | Host Configuration | Storage | Deployment Modules |
    | --------------------- | --------------------- | ----------------------- | -------- | ---- | -------------------------------- |
    | Federation 1 | 172.31.0.2 | CentOS 7.4 | 16C32G, one GPU card (not required) | 100G | kubernetes, mysql, iflearner-flow-server, iflearner-opeartor |
    | Federation 2 | 172.31.0.3 | CentOS 7.4 | 16C32G, one GPU card (not required) | 100G | kubernetes, mysql, iflearner-flow-federate, iflearner-opeartor |
    > Only the scene with only two federations is demonstrated here, which can be expanded freely

### 2.2 Host resources and operating system requirements
| **Category** | **Description** |
| -------- | ------------------------------------------------------------ |
| Host configuration | Not less than 8C, 31G, 50G, Gigabit network card, preferably GPU card for training acceleration |
| Operating System | CentOS linux 7.4 and above |
| File System | 1. The persistent data disk is mounted in the /data directory by default. <br/> 2. The free space of the root directory is not less than 20G. |
| System Parameters | 1. The number of file handles is not less than 65535. <br>2. The number of user processes is not less than 65535. |

### 2.3 Network Requirements
| Category | Description |
| ------------ | ------------------------------------------------------------ |
| Firewall Policy | 1. Firewall devices need to support long connections and unlimited connections. |

## 3. Project deployment (deployment in real scenarios)
In a real scenario, all parties are isolated and need to deploy a set of kubernetes clusters.

### 3.1 Deployment Diagram
![](images/iflearner-flow-deploy-arch.png)

### 3.2 Service side deployment
#### 3.2.1 Deploy kubernetes
Recommend a minimalist one-click deployment method [sealos](https://www.sealos.io/zh-Hans/docs/Intro)
> Currently supported version is 1.18

#### 3.2.2 Deploy iflearner-operator
See [iflearner-operator](https://github.com/iflytek/iflearner-operator)

#### 3.2.3 Deploy iflearner-flow-server
We provide a minimalist deployment method, please refer to [flow-server deployment and operation guide](https://github.com/iflytek/iflearner-flow/blob/main/deploy/in_standalone_kubernetes/iflearner_flow_server/README.md )

### 3.3 Federal side deployment
The implementation steps of each federal party are consistent, and the following are the implementation steps under a single federal party

#### 3.3.1 Deploy kubernetes
Recommend a minimalist one-click deployment method [sealos](https://www.sealos.io/zh-Hans/docs/Intro)
> Currently supported version is 1.18

#### 3.3.2 Deploy iflearner-operator
See [iflearner-operator](https://github.com/iflytek/iflearner-operator)

#### 3.3.3 Deploy iflearner-flow-federate
We provide a minimalist deployment method, please refer to [flow-federate deployment and operation guide](https://github.com/iflytek/iflearner-flow/blob/main/deploy/in_standalone_kubernetes/iflearner_flow_federate/README.md )

## 4. Project deployment (deployment under test and verification scenarios)
In the test and verification scenario, we can reuse a set of kubernetes clusters and perform test verification under the same cluster.

### 4.1 Deployment Diagram
![](images/iflearner-flow-deploy-arch1.png)