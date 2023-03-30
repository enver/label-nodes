# label-nodes
A simple application to label your EKS kubernetes nodes with `node-role.kubernetes.io/*` label as you can't set *kubernetes.io labels on AWS managed node groups as described:
* https://github.com/weaveworks/eksctl/issues/4007
* https://github.com/aws/containers-roadmap/issues/1451
* https://github.com/kubernetes/cloud-provider-aws/issues/110

As a workaround I set `node-role.kubernetes/foo=true` label while creating node group and use `label-nodes` application to attach `node-role.kubernetes.io/foo=true` to my node once node is up.

## Installation
Docker image can be found [here](https://hub.docker.com/r/enver/label-nodes)

There is a [helm chart](https://github.com/enver/charts) to help you deploying to the cluster
