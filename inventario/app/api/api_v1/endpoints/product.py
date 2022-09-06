from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException
from uuid import uuid4 as uuid
from app.schemas.response import GetResponse, PostResponse
from app.schemas.product import ProductCreate
from app.schemas.response import DeleteResponse
from app.schemas.response import PutResponse

router = APIRouter()

products: List[ProductCreate] = [
    ProductCreate(id=str(uuid()), product="Jabón", price=3, quantity=10, availabel=True, created_at=datetime.now()),
    ProductCreate(id=str(uuid()), product="Shampoo", price=10, quantity=5, availabel=True, created_at=datetime.now()),
    ProductCreate(id=str(uuid()), product="Cepillo", price=2, quantity=34, availabel=True, created_at=datetime.now())
]


@router.get('/product', response_model=GetResponse[List[ProductCreate]])
async def get_products():
    """
        Get all the product in the database
    """
    return GetResponse[List[ProductCreate]](data=products)


@router.post('/product', response_model=PostResponse[ProductCreate])
async def add_product(product: ProductCreate):
    """
        Add new product to the database
    """
    product.id: int = str(uuid())
    product.created_at: datetime = datetime.now() # momentaneo
    products.append(product.dict())
    
    return PostResponse[ProductCreate](data=products[-1])


@router.get('/product/{product_id}', response_model=GetResponse[ProductCreate])
async def get_product(product_id: str): 
    for product in products:
        if product_id == product.id:
            return GetResponse[ProductCreate](data=product)
    raise HTTPException(status_code=404, detail="Product doesn't exists")


@router.put('/product/{product_id}')
async def update_product(product_id: str, product: ProductCreate):
    index: int = 0
    for product_ in products:
        if product_id == product_.id:
            products[index] = product.dict()
            return PutResponse[ProductCreate](data=product)
        index += 1
    raise HTTPException(status_code=404, detail="Product cannot be updated")


@router.delete('/product/{product_id}', response_model=DeleteResponse[ProductCreate])
async def delete_product(product_id: str):
    index: int = 0
    for product in products:
        if product_id == product.id:
            products.pop(index)
            return DeleteResponse[ProductCreate](data=product)
        index += 1
    raise HTTPException(status_code=404, detail="Product cannot be deleted")
