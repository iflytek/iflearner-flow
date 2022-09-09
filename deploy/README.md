## Deployment guide

Currently, iflearner-flow is based on kubernetes and supports federated learning task scheduling on large-scale clusters.

The current deployment method mainly supports:
- Deployment in real scenarios (each party has an independent kubernetes cluster)
- Verify deployment in test scenarios (all parties share a kubernetes cluster)

### Deployment in real scenarios
Reference: [in_standalone_kubernetes](in_standalone_kubernetes/README.md)

### Verify the deployment in the test scenario
Reference: [all_in_one_kubernetes](all_in_one_kubernetes/README.md)