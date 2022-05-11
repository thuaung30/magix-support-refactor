from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from infrastructure.schemas.patient import Patient as PatientDTO
from infrastructure.models.patient.patient import Patient
from infrastructure.database import get_db

class PatientRepository:
    def __init__(self, db: Session=Depends(get_db)):
        self._db = db

    def create_patient(self, patient: PatientDTO) -> PatientDTO:
        db_patient = Patient(**patient.dict())
        self._db.add(db_patient)
        self._db.commit()
        return PatientDTO.from_orm(db_patient)
