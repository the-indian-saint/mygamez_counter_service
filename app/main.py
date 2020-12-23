from fastapi import FastAPI

from .storage import CounterStorage
memstorage = CounterStorage() # required by router

from .api import router

from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI(title="Counting Service", version="1.0.0")
app.add_middleware(PrometheusMiddleware)
app.add_route('/metrics', handle_metrics)

app.include_router(router, prefix="/v1")
