import os
from time import sleep
from datetime import datetime
from worker.worker import app


@app.task(priority=0)
def dummy_task(t: int):
    folder = "celery"
    os.makedirs(folder, exist_ok=True)
    sleep(t)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    with open(f"{folder}/{now}.txt", "w") as f:
        f.write("Hello, world!")


@app.task(priority=5)
def dummy_fail(t: int):
    sleep(t)
    raise ValueError("This task always fails.")
