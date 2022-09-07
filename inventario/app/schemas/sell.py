from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Sell(BaseModel):
    id: Optional[str]
    id_product: str # This is the foreign key
    quantity: int
    price: float
    total: float
    sell_date: Optional[datetime]
