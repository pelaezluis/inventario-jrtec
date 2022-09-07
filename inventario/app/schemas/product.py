from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    id: Optional[str]
    product: str
    price: float
    quantity: int
    available: bool = True
    created_at: Optional[datetime]