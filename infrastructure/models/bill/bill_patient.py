from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String 
from infrastructure.database import Base

class BillPatient(Base):
    __tablename__ = "bill_patients"

    id = Column(UUID(as_uuid=True), primary_key=True)
    meta_name = Column(String)
    meta_address = Column(String)
    meta_phone = Column(Integer)
    bill_id = Column(UUID(as_uuid=True), ForeignKey("bills.id", ondelete="CASCADE"))
    bill = relationship("Bill", back_populates="bill_patient")
    patient_id =  Column(UUID(as_uuid=True))
