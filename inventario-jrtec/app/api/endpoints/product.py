from fastapi import APIrouter

router = APIrouter()

@router.get('/product')
async def get_products():
    pass


@router.post('/product')
async def add_product():
    pass


@router.get('/product/{product_id}')
async def get_product(product_id: int):
    pass


@router.put('/product/{product_id}')
async def update_product(product_id: int):
    pass


@router.delete('/product/{product_id}')
async def delete_product(product_id: int):
    pass
