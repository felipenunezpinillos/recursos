from fastapi import FastAPI
from routers.recurso import router

app = FastAPI()

app.include_router(router)
