from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from infrastructure.schemas.uom import UOM as UOMDTO
from infrastructure.models.uom.uom import UOM

class UOMRepository:
    def __init__(self, db: Session=Depends(get_db)):
        self._db = db

    def create_uom(self, uom: UOMDTO) -> UOMDTO:
        db_uom = UOM(**uom.dict())
        self._db.add(db_uom)
        self._db.commit()
        return UOMDTO.from_orm(db_uom)
