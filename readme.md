# Creating a Cluster using Minikube
minikube start --cpus=6 --vm-driver hyperv --hyperv-virtual-switch "Primary Virtual Switch" --kubernetes-version=v1.16.10
minikube addons enable ingress
kubectl get all --all-namespaces


# deployment
kubectl apply -f ./deployment.yaml

# generate access port
kubectl port-forward pod/<generated pod name> 8010:5002

# testing 
get http://localhost:8010/docs

# service
kubectl apply -f ./service.yaml

# Minikube local (external address is the Minikube IP)
minikube ip

# testing
GET http://<minikube ip>:<service port>

# Watching
while (1) {clear; kubectl get all; sleep 2}