# Development guide
This document is mainly used for specification scripts in the development phase and guidelines for some tool scripts.

## Code normalization
Use some code normalization and detection tools to detect code specifications and adjust according to the prompts. The main steps are:

1. Auto format     
The isort, black, and docformatter tools are used to automatically adjust the specification of the specified code. The execution command is as follows:
    ```shell
    bash format.sh
    ````

2. Test Normalization    
Use isort, black, docformatter, mypy, and flake8 tools to standardize the specified code. The execution command is as follows:
    ```shell
    bash test.sh
    ````
    > Please follow the corresponding prompts to rectify.

## export swagger
Automatically export the rest interface schema file of `flask API` and automatically synchronize it to the doc directory for API documentation generation.

The execution command is as follows:    
```shell
bash export_swagger.sh
````

## export error code
The error codes defined in the `iflearner-flow` code are automatically exported and automatically synchronized to the doc directory for API documentation generation.

The execution command is as follows:    
```shell
bash export_errcode_md.sh
````