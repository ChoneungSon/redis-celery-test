import os
from datetime import datetime
from worker.worker import app
from worker.middleware import OnFailureTask

import asyncio


@app.task(base=OnFailureTask, priority=0)
def dummy_task(t: int):
    folder = "celery"
    os.makedirs(folder, exist_ok=True)
    asyncio.run(asyncio.sleep(t))
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    with open(f"{folder}/{now}.txt", "w") as f:
        f.write("Hello, world!")


# authoretry_for=(ValueError,)
# rate_limit='100/m'
@app.task(bind=True, base=OnFailureTask, priority=5, max_retries=5)
def dummy_fail(self, t: int):
    asyncio.run(asyncio.sleep(t))
    try:
        raise ValueError("This task always fails.")
    except Exception as e:
        raise self.retry(exc=e, countdown=10, max_retries=5)
