from pydantic import BaseModel
from pydantic.types import UUID4

# class Sex(str, Enum):
#     male = "male"
#     female = "female"

class BillItem(BaseModel):
    id: UUID4 
    meta_name: str | None = None
    meta_price: float | None = None
    meta_quantity: int = 0
    meta_subtotal: float | None = None

    class Config:
        orm_mode = True

class BillPatient(BaseModel):
    id: UUID4
    meta_patient_name: str | None = None
    meta_patient_address: str | None = None
    meta_patient_phone: str | None = None

    class Config:
        orm_mode = True

class Bill(BaseModel):
    total_amount: float | None = None
    status : str | None = None
    bill_items: list[BillItem]
    bill_patient: BillPatient

    class Config:
        orm_mode = True
