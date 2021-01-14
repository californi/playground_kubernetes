# loadbalancer
docker-compose up --build -d
docker ps


docker service create --name nginx-app --publish published=8080,target=80 --replicas=2 nginx
docker ps
PUBLIC_IP_ADDRESS:8080
