from fastapi import APIRouter, status, Depends
from infrastructure.schemas.uom import UOM as UOMDTO
from infrastructure.repositories.uom import UOMRepository
from usecases.uom import UOMUseCase

router = APIRouter(prefix="/uoms", tags=["UOMS"]) 

@router.post("createUOM", status_code=status.HTTP_200_OK, response_model=UOMDTO)
def create_patient(request: UOMDTO, repo=Depends(UOMRepository)):
    return UOMUseCase(repo).create_uom(request)

