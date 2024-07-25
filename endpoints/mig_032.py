from read_config_endpoints import load_endpoints
import asyncio

import json



    
async def mig_2():
    
    delay, status = await load_endpoints("MIG_1")
    
    if status:
        await asyncio.sleep(delay / 1000)
        
        response_data = {"MT": "MIG_1",
                        "MV": "123"}

        return response_data
    else:
        raise 'Эндпоинт отключен'