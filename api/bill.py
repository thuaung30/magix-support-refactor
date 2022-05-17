from fastapi import APIRouter, status, Depends
from infrastructure.schemas.bill import Bill as BillDTO
from infrastructure.repositories.bill import BillRepository
from infrastructure.repositories.sale_service_item import SaleServiceItemRepository
from infrastructure.repositories.patient import PatientRepository
from usecases.bill import BillUseCase

router = APIRouter(prefix="/bill", tags=["Bill"]) 

@router.post("/createBill", status_code=status.HTTP_200_OK, response_model=BillDTO)
def create_bill(
        request: BillDTO, 
        bill_repo=Depends(BillRepository), 
        sale_repo=Depends(SaleServiceItemRepository), 
        patient_repo=Depends(PatientRepository),
    ):
    return BillUseCase(bill_repo, sale_repo, patient_repo).create_bill(request)

