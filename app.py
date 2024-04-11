from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from worker.task import dummy_task, dummy_fail

app = FastAPI()


class TaskOut(BaseModel):
    id: str
    status: str


def _to_task_out(r: AsyncResult):
    return TaskOut(id=r.id, status=r.status)


@app.get("/start")
def start(t: int) -> TaskOut:
    r = dummy_task.delay(t)
    return _to_task_out(r)


@app.get("/start/fail")
def start_fail(t: int) -> TaskOut:
    r = dummy_fail.delay(t)
    return _to_task_out(r)
