import logging
from pydantic import BaseModel
import httpx
import time

# security and target
url_host = 'http://amdocsfailuremanager:5002'
# url_host = 'http://nginx-ingress.failure.svc'  # verificar depois o motivo do endereco nao funcionar nessa versao... talvez faltou algum compra de configuracao
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    while True:

        # defining data object
        failure = {"name": "aqui name",
                   "type": "aqui name",
                   "message": "aqui name",
                   "dateevent": "aqui name"}

        response = httpx.post(f"{url_host}/insufficientcpu",
                              headers=headers,
                              json=failure)

        logging.info(response)

        time.sleep(5)


if __name__ == '__main__':
    main()
