# Environment build and run
This document will guide how to build a docker image of the service and how to start a container of that image.

## build image
Image used to build iflearner_flow_server. In the current directory, execute the following script to complete the build:
```shell
bash build.sh 0.1
````

## run image
1. Preconditions: Complete the image construction.
2. Modification: You need to modify the `start.sh` script first, change the path of the configuration file, 
   log to the local actual path, as well as the exposed port, mirror, etc.
3. Execute: In the current directory, execute the following script to start the container:
```shell
bash start.sh
````