from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException
from uuid import uuid4 as uuid
from app.schemas.sell import Sell
from app.db.db import sells
from app.schemas.response import GetResponse, PostResponse, PutResponse, DeleteResponse

router = APIRouter()

@router.get('/sell', response_model=GetResponse[List[Sell]])
async def get_sells():
    """
        Get all the sells
    """
    return GetResponse[List[Sell]](data=sells)

@router.get('/sell/{sell_id}', response_model=GetResponse[Sell])
async def get_sell(sell_id: str):
    for sell in sells:
        if sell.id == sell_id:
            return GetResponse[Sell](data=sell)
    return HTTPException(status_code=404, detail="Sell doesn't exists")