from fastapi import Depends
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from infrastructure.schemas.sale_service_item import SaleServiceItem as SaleServiceItemDTO
from infrastructure.schemas.uom import UOM as UOMDTO
from infrastructure.schemas.category import Category as CategoryDTO
from infrastructure.models.sale_service_item.sale_service_item import SaleServiceItem
from infrastructure.models.sale_service_item.ssi_category import SSICategory
from infrastructure.models.sale_service_item.ssi_uom import SSIUOM
from infrastructure.models.uom.uom import UOM
from infrastructure.models.category.category import Category

class SaleServiceItemRepository:
    def __init__(self, db: Session=Depends(get_db)):
        self._db = db

    def create_sale_service_item(self, sale_service_item: SaleServiceItemDTO) -> SaleServiceItemDTO:
        db_uoms = []
        db_categories = []

        # fetch uom from db and convert to model list
        for uom in sale_service_item.ssi_uoms:
            db_uom = self._db.query(UOM).filter(UOM.id == uom.uom_id).first()
            uom_dto = UOMDTO.from_orm(db_uom)
            ssi_uom = SSIUOM(id=uom.id, meta_name=uom.meta_name if uom.meta_name else uom_dto.name, uom_id=uom.uom_id, ssi_id=sale_service_item.id)
            db_uoms.append(ssi_uom)

        # fetch category from db and convert to model list
        for category in sale_service_item.ssi_categories:
            db_category = self._db.query(Category).filter(Category.id == category.category_id).first()
            category_dto = CategoryDTO.from_orm(db_category)
            ssi_category = SSICategory(id=category.id, meta_name=category.meta_name if category.meta_name else category_dto.name, uom_id=category.category_id, ssi_id=sale_service_item.id)
            db_categories.append(ssi_category)

        db_sale_service_item = SaleServiceItem(id=sale_service_item.id, name=sale_service_item.name, price=sale_service_item.price, ssi_uoms=db_uoms, ssi_categories=db_categories)
        # implicitly save db_uoms and db_categories
        self._db.add(db_sale_service_item)
        self._db.commit()
        return SaleServiceItemDTO.from_orm(db_sale_service_item)

    def find_by_id(self, id: UUID4) -> SaleServiceItemDTO | None:
        sale_and_service_item = self._db.get(SaleServiceItem, id) 
        if(sale_and_service_item != None):
            return SaleServiceItemDTO.from_orm(sale_and_service_item)
        return None
