wget https://golang.org/dl/go1.15.6.linux-amd64.tar.gz
tar zxf go1.15.6.linux-amd64.tar.gz -C /usr/local
export PATH=$PATH:/usr/local/go/bin
GO111MODULE="on" go get sigs.k8s.io/kind@v0.9.0
export PATH=$PATH:~/go/bin
kind create cluster
snap install kubectl --classic

kind version

kubectl version
kubectl get nodes
