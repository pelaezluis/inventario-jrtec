from datetime import datetime
from typing import List
from uuid import uuid4 as uuid
from app.schemas.product import ProductCreate
from app.schemas.sell import Sell

id_product_1 = str(uuid())
id_product_2 = str(uuid())
id_product_3 = str(uuid())

products: List[ProductCreate] = [
    ProductCreate(id=id_product_1, product="Jabón", price=3, quantity=10, availabel=True, created_at=datetime.now()),
    ProductCreate(id=id_product_2, product="Shampoo", price=10, quantity=5, availabel=True, created_at=datetime.now()),
    ProductCreate(id=id_product_3, product="Cepillo", price=2, quantity=34, availabel=True, created_at=datetime.now())
]

sells: List[Sell] = [
    Sell(id=str(uuid()), id_product=id_product_2, quantity=1, price=2, total=2, sell_date=datetime.now()),
    Sell(id=str(uuid()), id_product=id_product_1, quantity=3, price=4, total=12, sell_date=datetime.now())
]