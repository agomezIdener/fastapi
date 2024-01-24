import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes import views

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

def configure():
    app.include_router(views.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="0.0.0.0", port=9001)
