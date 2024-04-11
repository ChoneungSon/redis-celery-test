from celery import Celery

app = Celery(__name__, broker="redis://redis:6379//", backend="redis://redis:6379/0", include=["worker.task"])

app.conf.update(
    broker_transport_options={
        "priority_steps": list(range(10)),
        "queue_order_strategy": "priority",
    },
    broker_pool_limit=10,
    worker_prefetch_multiplier=1,
    result_expires=10,
)
