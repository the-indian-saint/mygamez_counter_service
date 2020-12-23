from typing import List

from fastapi import APIRouter, Response

from .main import memstorage
from .schemas import Counter, CounterCreate

from starlette_exporter import PrometheusMiddleware, handle_metrics

#c = Counter('total_requests', 'Total Number of requests', ['method', 'endpoint'])

router = APIRouter()

#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()


@router.get("/counters", response_model=List[Counter])
def counters():
    #c.labels('get','/counters').inc()
    return memstorage.counters


@router.get("/counters/{name}")
def counters(name: str):
    #c.labels('get','/counters/{name}').inc()
    counter = memstorage.create_or_get_counter(name=name, createmode=False)
    if not counter:
        Response.status_code = 404
        return {'error': "missing counter"}
    return counter.count


@router.post("/counters", response_model=Counter)
def create_counter(data: CounterCreate):
    #c.labels('post','/counters').inc()
    return memstorage.create_or_get_counter(data.name)


@router.post("/counters/increment/{name}", response_model=Counter)
def increment_counter(name: str):
    #c.labels('post','/counters/increment/{name}').inc()
    counter = memstorage.increment_by_name(name)
    return counter

@router.post("/counters/decreament/{name}")
def decreament_counter(name: str):
    #c.labels('post','/counters/decreament/{name}').inc()
    counter = memstorage.decreament_by_name(name)
    if counter.count <= 0:
        return {name : "POW!!"}
    else:
        return counter

@router.post("/counters/reset/{name}", response_model=Counter)
def reset_counter(name: str):
    #c.labels('post','/counters/reset/{name}').inc()
    counter = memstorage.reset_by_name(name)
    return counter

@router.post("/counter/delete/{name}")
def delete_counter(name: str):
    #c.labels('post','/counters/reset/{name}').inc()
    memstorage.delete_counter_by_name(name)
    return {'Msg': f"{name} counter deleted"}

