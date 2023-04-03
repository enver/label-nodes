# label-nodes
A simple application to label your EKS Kubernetes nodes with `node-role.kubernetes.io/*` label as you can't set `*kubernetes.io` labels on AWS managed node groups as described:
* https://github.com/weaveworks/eksctl/issues/4007
* https://github.com/aws/containers-roadmap/issues/1451
* https://github.com/kubernetes/cloud-provider-aws/issues/110

As a workaround, set `node-role.kubernetes/foo=true` label while creating a node group and use the `label-nodes` application to attach `node-role.kubernetes.io/foo=true` to node once it is up.

## Installation
The docker image can be found [here](https://hub.docker.com/r/enver/label-nodes)

There is a [helm chart](https://github.com/enver/charts) to help you deploy to the cluster

## Customize
To customize the installation set
* INTERVAL_SECONDS - Interval at which the application runs and scans for new nodes (default `60`)
* SOURCE_LABEL_PREFIX - Source label prefix to be used for reading role (or any other information) (default `node-role.kubernetes/`)
* DESTINATION_LABEL_PREFIX - Destination label prefix (default `node-role.kubernetes.io/`)
