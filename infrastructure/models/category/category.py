from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from infrastructure.database import Base
from sqlalchemy.dialects.postgresql.base import UUID

class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    description = Column(String)
