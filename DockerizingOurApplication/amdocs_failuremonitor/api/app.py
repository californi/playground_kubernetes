from kubernetes import client, config, watch
import logging
from pydantic import BaseModel
import httpx
import re

# security and target
#url_host = 'http://amdocsfailuremanager:5002'
url_host = 'http://nginx-ingress.failure.svc'  # testar esse aqui....
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

           # defining data object
    failure = {"name": "aqui name",
                "type": "aqui name",
                "message": "aqui name",
                "dateevent": "aqui name"}

    response = httpx.post(f"{url_host}/insufficientcpu",
                                      headers=headers,
                                      json=failure)

    logging.info(response)


if __name__ == '__main__':
    main()
