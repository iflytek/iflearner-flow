## flow federate installation

We provide a quick deployment script `deploy.sh`, which is convenient for users to quickly deploy and verify.

### precondition
Flow-related components, some data need to be persistently stored, there are two cases here:
- If the kubernetes you build is a cluster, you need to build a distributed storage system in advance, such as distributed file storage system NFS, GLUSTERFS, etc.
- If the kubernetes you build is only a single machine, you can simplify and use only the local disk directory.

### Deployment
#### 1. Create PV
Here, we have built-in hostpath and nfs two pv templates for direct use in the case of kubernetes single machine and cluster.

##### Standalone (hostpath)
1. Create a local directory (**The remaining disk is at least 20g**), such as:
```shell
mkdir -p /data/iflearner
````

2. Modify the `spec.hostPath.path` field in the `components/pv/hostpath-pv.yaml` file to the directory location created in the first step. Of course, you can also modify the `spec.capacity.storage` field to
Dynamically adjust allocated storage space
   
3. Execute the following command to install:
```shell
kubectl apply -f components/pv/hostpath-pv.yaml
````
> If you want to uninstall, execute `kubectl delete -f components/pv/hostpath-pv.yaml`

##### Cluster (nfs)
1. Deploy an nfs cluster
   
2. Just modify the `spec.nfs.path` and `spec.nfs.server` fields in the `components/pv/nfs-pv.yaml` file according to the actual installed nfs. Of course, you can also modify the `spec as needed. capacity.storage` field to
Dynamically adjust allocated storage space
   
3. Execute the following command to install:
```shell
kubectl apply -f components/pv/nfs-pv.yaml
````
> If you want to uninstall, execute `kubectl delete -f components/pv/nfs-pv.yaml`

Note: **If you want to create other stored pv, just make sure the pv name is `flow-federate-pv`. **

#### 2. Execute the installation
Execute the following command in the current directory:
```shell
bash deploy.sh -i
````
Follow the prompts to select components to complete the quick installation:
```shell
Enter the install Component? pvc/mysql/flow_federate/all:
````
> You can choose to install the corresponding components separately (you need to install them in the order of pvc, mysql, flow_federate), or you can install them all at once (select all)

#### 3. Verify
You can view the status of deployed components by following the status check operation in the subsequent operation and maintenance steps.

The access address of flow_server is: **${any k8s host ip address}:31236**

### Operation and maintenance
#### Operation and maintenance commands
Execute `bash deploy.sh -h` to view the operation command, as follows:
```shell
Usage: flow federate deploy.sh [OPTIONS]
    Options:
        install -i install flow all compenont service
        status -s status flow all compenont service
        uninstall -u uninstall flow all compenont service
        help -h print usage
````
Currently, four types of commands are provided: install (installation), status (view status), uninstall (uninstallation), and help.

#### Uninstall components
Execute the following command in the current directory:
```shell
bash deploy.sh -u
````
Follow the prompts to select components to complete the quick uninstall:
```shell
Enter the uninstall Component? flow_federate/mysql/pvc/all:
````
> You can choose to uninstall the corresponding components separately (need to uninstall in the order of flow_federate, mysql, pvc), or uninstall them all at once (select all)

#### Status View
Execute the following command in the current directory:
```shell
bash deploy.sh -s
````
Follow the prompts to select components to complete the quick installation:
```shell
Enter the status Component? pvc/mysql/flow_federate/all:
````
> You can choose to view the corresponding components individually, or view them all (select all)