from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from infrastructure.schemas.bill import Bill as BillDTO
from infrastructure.models.bill.bill import Bill
from infrastructure.database import get_db

class BillRepository:
    def __init__(self, db: Session=Depends(get_db)):
        self._db = db

    def create_bill(self, bill: BillDTO) -> BillDTO:
        db_bill = Bill(**bill.dict())
        self._db.add(db_bill)
        self._db.commit()
        return BillDTO.from_orm(db_bill)
