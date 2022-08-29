# Environment build and run
This document will guide how to build a docker image of the service and start it on kubernetes.

## Deploy on kubernetes
1. Preconditions: Complete the image construction. See: [Building under docker](../docker/README.md)
2. Modification: You need to modify the `iflearner_flow_server.yaml` file, modify the corresponding mounted configuration file, log directory and mirror, etc.
3. Execute: Copy the image and the `iflearner_flow_server.yaml` file to the kubernetes cluster and execute the following command:
```shell
kubectl apply -f iflearner_flow_server.yaml
````