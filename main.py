from fastapi import FastAPI
import time
import asyncio
import os
import threading
from fastapi.concurrency import run_in_threadpool


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sync-io")
def sync_io():
    time.sleep(2)
    print("PID:", os.getpid())
    print("Thread:", threading.get_ident())
    return {"status": "done"}

@app.get("/async-io")
async def async_io():
    await asyncio.sleep(2)
    print("PID:", os.getpid())
    print("Thread:", threading.get_ident())
    return {"status": "done"}

def heavy_compute():
    total = 0
    for i in range(10**7):
        total += i
    return total

@app.get("/cpu-bound")
def cpu_bound():
    heavy_compute()
    print("PID:", os.getpid())
    print("Thread:", threading.get_ident())
    return {"status": "done"}

@app.get("/async-wrapper-cpu")
async def async_cpu():
    heavy_compute()
    print("PID:", os.getpid())
    print("Thread:", threading.get_ident())
    return {"status": "done"}