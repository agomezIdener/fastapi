from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services import service1,service2

router = APIRouter()

@router.get("/")
async def hello_world():
    return JSONResponse(content={"message": "Hello, Simple Example Get!"})

@router.post("/api/service1")
async def do_service1():
    result = await service1.run()
    return JSONResponse(content=result)

@router.get("/api/service2")
async def do_service2():
    # Asumiendo que `service2.run()` es una función que devuelve un diccionario.
    result = await service2.run()
    return JSONResponse(content=result)