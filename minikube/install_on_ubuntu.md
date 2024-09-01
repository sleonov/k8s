# Instructions
Tested on Ubuntu20 running as VM
Using virtual box as hypervisor
CPUs: 4
RAM: 16GB
Disk: 200GB

## Update user's profile 
```alias kubectl='minikube kubectl'```

## Install minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
sudo apt install docker.io
sudo usermod -aG docker $USER
```

## Install with virtualbox as driver (default profile)
2 Worker nodes, each with:
CPUs: 2
RAM: 4GB
Disk: 40GB
```
sudo apt install virtualbox
minikube start --driver=virtualbox \
               --kubernetes-version=v1.30 \
               --container-runtime=containerd \
               --cni=calico \
               --cpus=2 --memory=4g --disk-size=40g \
               -n 3
```

## Check Vms
```VBoxManage list vms```
Should see 3 VMs: 1 control plane, 2 workers

## Verify installation
```
minikube profile default
minikube status # 3 nodes: minikube, minikube-m02, minikube-m03
minikube node list # 3 nodes with IPs on virtual box bridge net
kubectl version 
minikube profile list # 1 profile "minikube" / 3 nodes
minikube logs # display k8s start logs
minikube ssh # login for debugging to control plane node
```

## Install add-ons
```
minikube addons list
minikube addons enable metrics-server
minikube addons enable dashboard
```
