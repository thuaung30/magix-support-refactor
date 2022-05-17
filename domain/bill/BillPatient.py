from pydantic.types import UUID4


class BillPatient:
    def __init__(
            self,
            id: UUID4,
            meta_patient_name: str,
            meta_patient_address: str,
            meta_patient_phone: str,
            patient_id: UUID4
        ):
        self.id = id
        self.meta_patient_name = meta_patient_name
        self.meta_patient_address = meta_patient_address 
        self.meta_patient_phone = meta_patient_phone 
        self.patient_id = patient_id


    def set_meta_patient_name(self, name: str):
        self.meta_patient_name = name

    def set_meta_patient_address(self, address: str):
        self.meta_patient_address = address

    def set_meta_patient_phone(self, phone: str):
        self.meta_patient_phone = phone

    def asdict(self):
        return { 
            "id": self.id,
            "meta_patient_name": self.meta_patient_name,
            "meta_patient_address": self.meta_patient_address,
            "meta_patient_phone": self.meta_patient_phone,
            "patient_id": self.patient_id
        }
