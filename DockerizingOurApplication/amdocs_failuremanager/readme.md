# Building and deploying in docker hub
docker build -t amdocs_failuremanager .
docker tag amdocs_failuremanager californibrs/amdocs_failuremanager
docker push californibrs/amdocs_failuremanager
docker run -d --name amdocs_failuremanager -p 8000:5002 californibrs/amdocs_failuremanager

# testing
get http://localhost:8000/docs


