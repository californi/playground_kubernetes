from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
import logging
from pydantic import BaseModel
import os
import socket

app = FastAPI()
Instrumentator().instrument(app).expose(app)


print(socket.gethostname())

class Failure(BaseModel):
    name: str
    type: str
    message: str
    dateevent: str


@app.get("/")
def helloamdocs():
    message = "Application: {0}, Host: {1} \n".format(os.environ['APP'], socket.gethostname())
    return message


@app.post("/insufficientcpu")
async def create_failure_insufficientCPU(request: Failure):
    logging.warn(request)
    return "Waiting for metacontroller probe."
