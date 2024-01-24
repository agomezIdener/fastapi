import asyncio

async def run():
    # Realiza alguna operación de bloqueo con asyncio, por ejemplo:
    await asyncio.sleep(1)  # Simula una operación de bloqueo
    return {"status": "ok", "data": "Service executed successfully"}
