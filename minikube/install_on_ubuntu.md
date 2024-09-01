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
1 Control plane, 1 Worker node with:
CPUs: 2
RAM: 6GB
Disk: 80GB
```
sudo apt install virtualbox
minikube start --driver=virtualbox \
  --kubernetes-version=v1.30 \
  --container-runtime=containerd \
  --cni=calico \
  --cpus=2 --memory=6g --disk-size=80g \
  -n 2
```

## Check Vms
```
# Should see 2 VMs: 1 control plane, 1 worker
VBoxManage list vms
```

## Verify installation
```
minikube profile default

# 2 nodes: minikube, minikube-m02
minikube status

# 2 nodes with IPs on virtual box bridge net
minikube node list

kubectl version

# 1 profile "minikube" / 2 nodes
minikube profile list

# display k8s start logs
minikube logs

# display k8s start logs
minikube ssh
```

## Install add-ons
```
minikube addons list
minikube addons enable metrics-server
minikube addons enable dashboard

# Show dashboard URL
minikube dashboard --url
```
