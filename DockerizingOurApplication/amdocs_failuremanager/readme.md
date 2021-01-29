# Building and publishing in docker hub
docker build -t amdocsfailuremanager .
docker tag amdocsfailuremanager californibrs/amdocsfailuremanager
docker push californibrs/amdocsfailuremanager





# testing
docker run -d --name amdocs_failuremanager -p 8000:5002 californibrs/amdocs_failuremanager

get http://localhost:8000/docs


# Using another set of tags
# docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
docker tag amdocs_failuremanager californi/amdocs_failuremanager:v1
docker tag amdocs_failuremanager californi/amdocs_failuremanager:v2
docker tag amdocs_failuremanager californi/amdocs_failuremanager:v3
docker tag amdocs_failuremanager californi/amdocs_failuremanager:v4