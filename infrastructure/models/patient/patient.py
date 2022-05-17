from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Enum, Integer, String
from infrastructure.database import Base
import enum

class Sex(str, enum.Enum):
    male = "male"
    female = "female"

class Patient(Base):
    __tablename__ = "patients"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    sex = Column(Enum(Sex))
    age = Column(Integer)
    contact_details = Column(String)
    address = Column(String)
