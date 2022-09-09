from email.mime import audio
from fastapi import APIRouter
from app.api.api_v1.endpoints import product, sell, audio_converter

api_router = APIRouter()

api_router.include_router(product.router, tags=['product'])
api_router.include_router(sell.router, tags=['sell'])
api_router.include_router(audio_converter.router, tags=['audioConverter'])
