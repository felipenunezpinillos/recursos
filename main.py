from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database
from sqlalchemy.sql import select
from routers.recurso import router
import asyncio

app = FastAPI()

app.include_router(router)

USERNAME = 'monitoring-user'
PASSWORD = 'isis2503'
NAME_MEW = '10.50.240.15'
NAME_DB = 'recursos-db'
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{NAME_MEW}:5432/{NAME_DB}"

print(DATABASE_URL)
metadata=MetaData()
database = Database(DATABASE_URL)


async def startup_db():
    try:
        await database.connect()
        return database
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise

