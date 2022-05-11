from fastapi import APIRouter, status, Depends
from infrastructure.schemas.sale_service_item import SaleServiceItem as SaleServiceItemDTO
from infrastructure.repositories.sale_service_item import SaleServiceItemRepository
from usecases.sale_service_item import SaleServiceItemUseCase

router = APIRouter(prefix="/saleServiceItems", tags=["Sale Service Items"]) 

@router.post("createSaleServiceItems", status_code=status.HTTP_200_OK, response_model=SaleServiceItemDTO)
def create_patient(request: SaleServiceItemDTO, repo=Depends(SaleServiceItemRepository)):
    return SaleServiceItemUseCase(repo).create_sale_service_item(request)

