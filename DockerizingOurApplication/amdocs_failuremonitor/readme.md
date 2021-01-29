# Building and publishing in docker hub
docker build -t amdocsfailuremonitor .
docker tag amdocsfailuremonitor californibrs/amdocsfailuremonitor
docker push californibrs/amdocsfailuremonitor




# testing
kubectl logs <generated pod name>
#docker run -d --name amdocs_failuremonitor -p 8020:5001 californibrs/amdocs_failuremonitor