from fastapi import APIRouter, status, Depends
from infrastructure.schemas.patient import Patient as PatientDTO
from infrastructure.repositories.patient import PatientRepository
from usecases.patient import PatientUseCase

router = APIRouter(prefix="/patient", tags=["Patient"]) 

@router.post("/createPatient", status_code=status.HTTP_200_OK, response_model=PatientDTO)
def create_patient(request: PatientDTO, repo=Depends(PatientRepository)):
    return PatientUseCase(repo).create_patient(request)

