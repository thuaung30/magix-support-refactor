from enum import Enum
from pydantic import BaseModel
from pydantic.types import UUID4

class Sex(str, Enum):
    male = "male"
    female = "female"

class Patient(BaseModel):
    id: UUID4
    name: str 
    sex: Sex = Sex.male
    age: int
    contact_details: str
    address: str

    class Config:
        orm_mode = True
