# Label Nodes
Label Nodes is a tool designed to help users label Kubernetes nodes that are managed by Amazon Elastic Kubernetes Service (EKS). EKS does not allow users to set the `kubernetes.io` labels for managed node groups. Instead, users can set some other label and use the label-nodes project to set the appropriate `*.kubernetes.io/` label.

Issue references:
* https://github.com/weaveworks/eksctl/issues/4007
* https://github.com/aws/containers-roadmap/issues/1451
* https://github.com/kubernetes/cloud-provider-aws/issues/110

## How it Works
The Label Nodes tool works by using the Kubernetes API to get a list of nodes in the cluster. The tool then updates the selected node's labels to include the `node-role.kubernetes.io/` label with the specified category and value using predefined source label

## Installation
### Local
To install Label Nodes, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/enver/label-nodes.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Kubernetes configuration file (if you haven't already):
```bash
export KUBECONFIG=<path-to-your-kubeconfig-file>
```

#### Customize
To customize the installation set
* INTERVAL_SECONDS - Interval at which the application runs and scans for new nodes (default `60`)
* SOURCE_LABEL_PREFIX - Source label prefix to be used for reading role (or any other information) (default `node-role.kubernetes/`)
* DESTINATION_LABEL_PREFIX - Destination label prefix (default `node-role.kubernetes.io/`)

### Docker
The docker image can be found [here](https://hub.docker.com/r/enver/label-nodes)

There is a [helm chart](https://github.com/enver/charts) to help you deploy to the Kubernetes cluster.

## Usage
To use Label Nodes, follow these steps:

Run the label-nodes.py script:
```bash
python label-nodes.py
```

## Example
Create managed EKS node group and set role label `node-role.kubernetes/foo=true`. Once label-nodes is deployed it will set `node-role.kubernetes.io/foo=true` to all running nodes where `node-role.kubernetes/foo=true` exists. Then `kubectl get nodes` will show node role 

```
# kubectl get nodes                               ↓
NAME                                   STATUS   ROLES             AGE     VERSION
ip-1-2-3-4.<region>.compute.internal   Ready    foo                1m     v1.2.3
....
```

Verify that the label has been applied to the node by running the kubectl describe node <node-name> command.

## Contributing
If you would like to contribute to Label Nodes, please fork the repository and submit a pull request with your changes. Contributions are always welcome!

## License
Label Nodes is licensed under the MIT license. See the LICENSE file for more details.
