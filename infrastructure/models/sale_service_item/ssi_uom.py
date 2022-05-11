from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from infrastructure.database import Base

class SSIUOM(Base):
    __tablename__ = "sale_service_items_uoms"

    id = Column(UUID(as_uuid=True), primaryKey=True)
    meta_name = Column(String)
    ssi_id = Column(UUID(as_uuid=True), ForeignKey("sale_service_items.id", ondelete="CASCADE"))
    ssi = relationship("SaleServiceItem", back_populates="ssi_uoms")
    uom_id = Column(UUID(as_uuid=True))
