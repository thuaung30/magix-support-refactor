from fastapi import APIRouter
from . import bill, patient, sale_service_item, category, uom

router = APIRouter(prefix="/api")

router.include_router(bill.router)
router.include_router(patient.router)
router.include_router(sale_service_item.router)
router.include_router(category.router)
router.include_router(uom.router)
