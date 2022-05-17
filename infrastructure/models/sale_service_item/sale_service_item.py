from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.sql.sqltypes import Float, String
from infrastructure.database import Base

class SaleServiceItem(Base):
    __tablename__ = "sale_service_items"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    price = Column(Float)
    ssi_uoms = relationship("SSIUOM", back_populates="ssi", cascade="save-update, delete")
    ssi_categories = relationship("SSICategory", back_populates="ssi", cascade="save-update, delete")
