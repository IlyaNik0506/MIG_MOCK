import os
import asyncio
from delay_endpoints import update_endpoint_delay
from fastapi import FastAPI, Request, BackgroundTasks, Body
from disable_endpoints import disable_endpoints, enable_endpoints

import uvicorn
import time

from endpoints.mig_032 import mig_2
from endpoints.mig_056 import mig_1

from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

instrumentator = Instrumentator().instrument(app)

@app.post("/RReq")
async def mig_68():
    return await mig_1()

@app.post("/AReq")
async def mig_56():
    return await mig_2()

@app.post("/delay")
async def delay(endpoint_name: str = Body(...), delay: int = Body(...)):
    await update_endpoint_delay(endpoint_name, delay)
    return f'Время ответа изменено на {delay}'


@app.post("/disable")
async def disable(endpoint: str = Body(...), delay: int = Body(...)):
    await disable_endpoints(endpoint)
    await asyncio.sleep(delay)
    await enable_endpoints(endpoint)
    
# Экспонируем метрики Prometheus
instrumentator.expose(app, include_in_schema=False)

# Запуск приложения
if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, workers=1, log_level="info")