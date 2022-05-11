from infrastructure.repositories.sale_service_item import SaleServiceItemRepository
from infrastructure.schemas.sale_service_item import SaleServiceItem as SaleServiceItemDTO;

class SaleServiceItemUseCase:
    def __init__(self, repo:SaleServiceItemRepository):
        self._repo = repo

    def create_sale_service_item(self, sale_service_item: SaleServiceItemDTO) -> SaleServiceItemDTO:
        return self._repo.create_sale_service_item(sale_service_item)
