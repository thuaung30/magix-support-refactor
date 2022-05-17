from pydantic import BaseModel
from pydantic.types import UUID4

class SSIUOM(BaseModel):
    id: UUID4 | None
    meta_name: str | None
    uom_id: UUID4

    class Config:
        orm_mode = True

class SSIUOMCategory(BaseModel):
    id: UUID4 | None
    meta_name: str | None
    category_id: UUID4
    
    class Config:
        orm_mode = True

class SaleServiceItem(BaseModel):
    id: UUID4
    name: str 
    price: float
    ssi_uoms: list[SSIUOM] = []
    ssi_categories: list[SSIUOMCategory] = []

    class Config:
        orm_mode = True
