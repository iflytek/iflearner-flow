## flow federate安装

我们提供了个一键式的部署脚本`deploy.sh`，便于用户快速部署验证。

### 前置条件
flow相关组件，一些数据都需要持久化存储, 这里分两种情况: 
- 如果您搭建的kubernetes是集群的话，**需要您预先搭建好一套分布式存储系统**， 如分布式文件存储系统NFS、GLUSTERFS等。
- 如果您搭建的kubernetes只是单机的话，可以简化只使用本地磁盘目录即可。

### 部署
#### 1. 创建PV
这里我们针对kubernetes单机和集群两种情况，分别内置了hostpath和nfs两种pv模板直接使用。
##### 单机(hostpath)
1. 创建一个本地目录(**所在盘剩余至少大于20g**),如:
```shell
mkdir -p /data/iflearner
```
2. 修改`components/pv/hostpath-pv.yaml`文件中`spec.hostPath.path`字段为第一步创建的目录位置即可, 当然也可以修改`spec.capacity.storage`字段来
动态调整分配的存储空间
3. 执行下述命令进行安装即可:
```shell
kubectl apply -f components/pv/hostpath-pv.yaml
```
> 如果想卸载, 执行`kubectl delete -f components/pv/hostpath-pv.yaml`即可

##### 集群(nfs)
1. 搭建好nfs集群
2. 只需要根据实际安装的nfs, 修改`components/pv/nfs-pv.yaml`文件中`spec.nfs.path`和`spec.nfs.server`字段即可, 当然也可以根据需要修改`spec.capacity.storage`字段来
动态调整分配的存储空间
3. 执行下述命令进行安装即可:
```shell
kubectl apply -f components/pv/nfs-pv.yaml
```
> 如果想卸载, 执行`kubectl delete -f components/pv/nfs-pv.yaml`即可

注意: **如果想创建其它存储的pv也可，只需要保证pv名称为`flow-federate-pv`即可。**

#### 2. 执行安装
在当前目录下执行下述命令:
```shell
bash deploy.sh -i
```
按提示选择组件即可完成快速安装:
```shell
Enter the install Component? pvc/mysql/flow_federate/all:
```
> 可选择对应的组件分别安装(需按照pvc、mysql、flow_federate的顺序安装), 也可全部一次性安装(选择all)

#### 3. 验证
您可以按照后续运维步骤的状态查看操作，查看部署的组件状态。

flow_federate的访问地址为: **${任一k8s主机ip地址}:31236**

### 运维
#### 运维命令
执行`bash deploy.sh -h`即可查看操作命令，如下所示:
```shell
Usage: flow federate deploy.sh [OPTIONS]
    Options:
        install         -i               install    flow all compenont service
        status          -s             status     flow all compenont service
        uninstall       -u               uninstall  flow all compenont service
        help            -h               print usage
```
当前提供install(安装)、status(查看状态)、uninstall(卸载)、help四类命令。

#### 卸载组件
在当前目录下执行下述命令:
```shell
bash deploy.sh -u
```
按提示选择组件即可完成快速卸载:
```shell
Enter the uninstall Component? flow_federate/mysql/pvc/all: 
```
> 可选择对应的组件分别卸载(需按照flow_federate、mysql、pvc的顺序卸载), 也可全部一次性卸载(选择all)

#### 状态查看
在当前目录下执行下述命令:
```shell
bash deploy.sh -s
```
按提示选择组件即可完成快速安装:
```shell
Enter the status Component? pvc/mysql/flow_federate/all: 
```
> 可选择对应的组件分别查看, 也可全部查看(选择all)