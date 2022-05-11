from fastapi import Depends
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from infrastructure.schemas.category import Category as CategoryDTO
from infrastructure.models.category.category import Category

class CategoryRepository:
    def __init__(self, db: Session=Depends(get_db)):
        self._db = db

    def create_category(self, category: CategoryDTO) -> CategoryDTO:
        db_category = Category(**category.dict())
        self._db.add(db_category)
        self._db.commit()
        return db_category
