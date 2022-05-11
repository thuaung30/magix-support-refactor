from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer, String 
from infrastructure.database import Base

class BillItem(Base):
    __tablename__ = "bill_items"

    id = Column(UUID(as_uuid=True), primaryKey=True)
    meta_name = Column(String)
    meta_price = Column(Float)
    meta_quantity = Column(Integer)
    meta_subtotal = Column(Float)
    bill_id = Column(UUID(as_uuid=True), ForeignKey("bills.id", ondelete="CASCADE"))
    bill = relationship("Bill", back_populates="bill_items")
    ss_id =  Column(UUID(as_uuid=True))
