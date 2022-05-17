from sqlalchemy import Column, Float
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Enum
from infrastructure.database import Base
import enum

class Status(str, enum.Enum):
    draft = "draft"
    outstanding = "completed"
    cancelled = "cancelled"

class Bill(Base):
    __tablename__ = "bills"

    id = Column(UUID(as_uuid=True), primary_key=True)
    total_amount = Column(Float)
    status = Column(Enum(Status))
    bill_patient = relationship("BillPatient", back_populates="bill", cascade="delete")
    bill_items = relationship("BillItem", back_populates="bill", cascade="delete")
