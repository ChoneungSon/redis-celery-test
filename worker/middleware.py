from celery import Task
from celery.worker.request import Request


class OnFailureTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print("task_id", task_id)
        return super().on_success(retval, task_id, args, kwargs)
        # slack event

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("task_id", task_id)
        return super().on_failure(exc, task_id, args, kwargs, einfo)
        # slack event
