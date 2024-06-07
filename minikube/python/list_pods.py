#!/usr/bin/env python3

from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

api = client.CoreV1Api()
ret = api.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print(f"{i.status.pod_ip},{i.metadata.namespace},{i.metadata.name}")
