import aiofiles
import json

async def update_endpoint_delay(name, new_delay):
    async with aiofiles.open('data/config_endpoints.json', 'r') as file:
        config_str = await file.read()
    config = json.loads(config_str)

    found = False
    for item in config:
        if item['name'] == name:
            item['delay'] = new_delay  
            found = True
            break

    if not found:
        raise ValueError(f"Конечная точка '{name}' не найдена")


    async with aiofiles.open('data/config_endpoints.json', 'w') as file:
        await file.write(json.dumps(config, indent=4))