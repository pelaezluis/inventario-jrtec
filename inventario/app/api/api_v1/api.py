from fastapi import APIRouter
from app.api.api_v1.endpoints import product

api_router = APIRouter()

api_router.include_router(product.router, tags=['product'])
