from infrastructure.repositories.uom import UOMRepository
from infrastructure.schemas.uom import UOM as UOMDTO;

class UOMUseCase:
    def __init__(self, repo: UOMRepository):
        self._repo = repo

    def create_uom(self, uom: UOMDTO) -> UOMDTO:
        return self._repo.create_uom(uom)
