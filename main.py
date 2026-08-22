from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.routers.auth import authRouter



@asynccontextmanager
async def lifespan(app:FastAPI):
    # initialize DB at Start
    create_tables()
    yield #seperation point



app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter, tags=["auth"], prefix="/auth")




@app.get("/health")
def health_check():
    return {"status": "Running"}
