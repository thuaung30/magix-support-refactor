from infrastructure.repositories.patient import PatientRepository
from infrastructure.schemas.patient import Patient as PatientDTO;

class PatientUseCase:
    def __init__(self, repo: PatientRepository):
        self._repo = repo

    def create_patient(self, patient: PatientDTO) -> PatientDTO:
        return self._repo.create_patient(patient)
