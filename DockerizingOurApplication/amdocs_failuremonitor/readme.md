# Building and deploying in docker hub
docker build -t amdocs_failuremonitor .
docker tag amdocs_failuremonitor californibrs/amdocs_failuremonitor
docker push californibrs/amdocs_failuremonitor


#docker run -d --name amdocs_failuremonitor -p 8020:5001 californibrs/amdocs_failuremonitor

# testing
kubectl logs <generated pod name>