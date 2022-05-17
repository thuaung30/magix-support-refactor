from infrastructure.repositories.bill import BillRepository
from infrastructure.repositories.sale_service_item import SaleServiceItemRepository
from infrastructure.repositories.patient import PatientRepository
from infrastructure.schemas.bill import Bill as BillDTO
from domain.bill.Bill import Bill
from domain.bill.BillPatient import BillPatient
from domain.bill.BillItem import BillItem
from uuid import uuid4

class BillUseCase:
    def __init__(
            self, 
            bill_repo: BillRepository, 
            sale_repo: SaleServiceItemRepository,
            patient_repo: PatientRepository
        ):
        self._bill_repo = bill_repo
        self._sale_repo = sale_repo
        self._patient_repo = patient_repo

    def create_bill(self, _bill: BillDTO) -> BillDTO:
        patient = self._patient_repo.find_by_id(_bill.bill_patient.id)
        if patient == None:
            # throw some kind of exception here
            raise Exception("some kind of exception")
        patient = BillPatient(
            id=uuid4(),
            meta_patient_name=patient.name if _bill.bill_patient.meta_patient_name == None else _bill.bill_patient.meta_patient_name,
            meta_patient_address=patient.address if _bill.bill_patient.meta_patient_address == None else _bill.bill_patient.meta_patient_address,
            meta_patient_phone=patient.contact_details if _bill.bill_patient.meta_patient_phone == None else _bill.bill_patient.meta_patient_phone,
            patient_id=patient.id
            )
        items = []
        for item in _bill.bill_items:
            sale_service_item = self._sale_repo.find_by_id(item.id)
            if sale_service_item == None:
                # thow some kind of exception here
                raise Exception("some kind of exception")
            bill_item = BillItem(
                id=uuid4(),
                ss_id=sale_service_item.id,
                meta_name=sale_service_item.name if item.meta_name == None else item.meta_name,
                meta_price=sale_service_item.price if item.meta_price ==  None else item.meta_price,
                meta_quantity=item.meta_quantity if item.meta_quantity == None else item.meta_quantity
            )
            items.append(bill_item)

        if len(items) <= 0:
            raise Exception("item list cannot be empty")

        bill = Bill(
            id=uuid4(),
            total_amount=sum(item.meta_subtotal for item in items),
            status="draft",
            bill_items=items,
            bill_patient=patient
                )
        bill_dto = BillDTO(**bill.asdict())
        return self._bill_repo.create_bill(bill_dto)
