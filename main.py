from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables




@asynccontextmanager
async def lifespan(app:FastAPI):
    # initialize DB at Start
    create_tables()
    yield #seperation point



app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "Running"}
