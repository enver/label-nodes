#!/usr/bin/env python
###############################################################################
import os
import time
import logging
from kubernetes import config
from kubernetes import client

logging.basicConfig(level=os.environ.get('LOG_LEVEL', 'INFO').upper())

###############################################################################
if __name__ == '__main__':
    interval = int(os.getenv('SOURCE_LABEL_PREFIX', 60))
    source_label_prefix = os.getenv('SOURCE_LABEL_PREFIX', 'node-role.kubernetes/')
    destination_label_prefix = os.getenv('DESTINATION_LABEL_PREFIX', 'node-role.kubernetes.io/')

    config.load_kube_config()
    logger = logging.getLogger('relabel')
    
    while True:
        try:
            api_instance = client.CoreV1Api()
            node_list = api_instance.list_node()
            for node in node_list.items:
                relabeled = False
                for key, val in node.metadata.labels.items():
                    if key.startswith(source_label_prefix):
                        role = key.split('/')[1]
                    if key.startswith(destination_label_prefix):
                        relabeled = True
                if not relabeled:
                    body = {
                        "metadata": {
                            "labels": {
                                f"{destination_label_prefix.rstrip('/')}/{ role }": "true"
                            }
                        }
                    }
                    logger.info(f'Patching node { node.metadata.name } with {body.get("metadata").get("labels")}')
                    api_instance.patch_node(node.metadata.name, body)
        except Exception as ex:
            print(ex)
        time.sleep(interval)