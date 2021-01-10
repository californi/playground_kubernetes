from kubernetes import client, config, watch
import logging
from pydantic import BaseModel
import httpx
import re

# security and target
url_host = 'http://amdocsfailuremanager:5002'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    # accesing the cluster
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    w = watch.Watch()

    for event in w.stream(v1.list_event_for_all_namespaces):
        if event['object'].type == "Warning":

            # defining data object
            failure = {"name": event['object'].metadata.name,
                       "type": event['object'].type,
                       "message": event['object'].message,
                       "dateevent": str(event['object'].metadata.creation_timestamp)}

            # characterising and analysing data object
            resultNamePod = re.search(
                'kube-znn', str(failure["name"]), re.IGNORECASE)
            resultMessageCPU = re.search(
                'Insufficient cpu', str(failure["message"]), re.IGNORECASE)

            # decision make
            if resultNamePod and resultMessageCPU:
                print("falha encontrada")
                logging.warning(failure)
                response = httpx.post(f"{url_host}/insufficientcpu",
                                      headers=headers,
                                      json=failure)

    logging.info("Finished pod stream.")


if __name__ == '__main__':
    main()
