from src.domain.BillItem import BillItem
from src.domain.BillPatient import BillPatient

class Bill:
    def __init__(
            self, 
            id: str | None, 
            total_amount: float = 0, 
            status: str | None = None,
            bill_items: list[BillItem] = [],
            bill_patient: BillPatient | None = None,
        ):
        self.id = id
        self.total_amount = total_amount
        self.status = status
        self.bill_items = bill_items
        self.bill_patient = bill_patient

    def add_patient(self, patient: BillPatient):
        self.bill_patient = patient

    def remove_patient(self):
        self.bill_patient = None

    def set_patient_name(self, name: str): 
        if self.bill_patient != None:
            self.bill_patient.set_meta_patient_name(name)

    def set_patient_phone(self, phone: str): 
        if self.bill_patient != None:
            self.bill_patient.set_meta_patient_phone(phone)

    def set_patient_address(self, address: str): 
        if self.bill_patient != None:
            self.bill_patient.set_meta_patient_address(address)

    def _calculate_total_amount(self):
        self.total_amount += sum(bill_item.get_meta_subtotal() for bill_item in self.bill_items)

    def add_bill_item(self, item: BillItem):
        self.bill_items.append(item) 
        self._calculate_total_amount()

    def remove_bill_item(self, index: int):
        if index >= 0 and index < len(self.bill_items):
            self.bill_items.pop(index)
            self._calculate_total_amount()

    def modify_quantity(self, qty: int, index: int):
        if index >= 0 and index < len(self.bill_items) and qty <= 0:
            self.bill_items[index].modify_quantity(qty)
            self._calculate_total_amount()

    def asdict(self):
        return {
            "id": self.id,
            "total_amount": self.total_amount,
            "status": self.status,
            "bill_item": [bill_item.asdict() for bill_item in self.bill_items],
            "bill_patient": self.bill_patient.asdict() if self.bill_patient != None else None
        }
