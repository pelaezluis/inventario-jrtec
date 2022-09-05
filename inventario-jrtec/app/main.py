from fastapi import FastAPI
from api.api_v1.api import api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "To see endpoints go to this link: localhost:8000/docs"}

app.include_router(api_router)