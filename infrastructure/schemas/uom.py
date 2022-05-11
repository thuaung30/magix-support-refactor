from pydantic import BaseModel
from pydantic.types import UUID4

class UOM(BaseModel):
    id: UUID4 | None
    name: str
    description: str
