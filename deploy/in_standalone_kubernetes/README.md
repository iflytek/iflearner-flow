## Deployment in real scenarios

`iflearner-flow`, is divided into two roles (`flow-server`, `flow-federate`), among which:
- `flow-server` is the central end, mainly used for model aggregation and process control of all parties
- `flow-federate` is the federation side, which is a specific federation task party, mainly for actual federation task training.

The `iflearner_flow_server` involved is the component that implements the `flow_server` role, and `iflearner_flow_federate` is the component that implements the `flow_federate` role.
in:
- `iflearner_flow_server` is the central side, **only need to deploy one set**
- `iflearner_flow_federate`** requires a separate set of deployments on each federation side**.

### precondition
- install kubernetes>=1.18
- install iflearner-operator

For details, please refer to: [Online Installation and Deployment](https://iflytek.github.io/iflearner-flow/installation/online_on_kubernetes_installation/)

### Deploy iflearner_flow_server
See: [iflearner_flow_server](iflearner_flow_server/README.md)

### deploy iflearner_flow_federate
See: [iflearner_flow_federate](iflearner_flow_federate/README.md)