from datetime import datetime
from fastapi import APIRouter
from uuid import uuid4 as uuid
from .productSchema import ProductCreate

router = APIRouter()

products = [
    {
        'id': str(uuid()),
        'product': 'Jabón',
        'price': 3,
        'quantity': 10,
        'available': True,
        'created_at': datetime.now()
    },
    {
        'id': str(uuid()),
        'product': 'Shampoo',
        'price': 10,
        'quantity': 5,
        'available': True,
        'created_at': datetime.now()
    },
    {
        'id': str(uuid()),
        'product': 'Cepillo',
        'price': 2,
        'quantity': 34,
        'available': True,
        'created_at': datetime.now()
    }
]



@router.get('/product')
async def get_products():
    """
        Get all the product in the database
    """
    return products


@router.post('/product')
async def add_product(product: ProductCreate):
    """
        Add new product to the database
    """
    product.id = str(uuid())
    product.created_at = datetime.now() # momentaneo
    products.append(product.dict())
    return products[-1]


@router.get('/product/{product_id}')
async def get_product(product_id: str):
    for product in products:
        if product_id == product["id"]:
            return product
    return "Product doesn't exist!"


@router.put('/product/{product_id}')
async def update_product(product_id: str):
    pass


@router.delete('/product/{product_id}')
async def delete_product(product_id: str):
    index = 0
    for product in products:
        if product_id == product["id"]:
            products.pop(index)
        index += 1
    return "Product deleted!"
