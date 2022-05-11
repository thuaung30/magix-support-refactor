class Patient:
    def __init__(
            self,
            id: str,
            name: str,
            sex: str,
            contact_details: str | None,
            address: str | None,
            age: int = 30,
        ):
        self.id = id
        self.name = name
        self.sex = sex
        self.contact_details = contact_details
        self.address = address
        self.age = age

    def modify_patient(
            self,
            id: str,
            name: str,
            sex: str,
            contact_details: str | None,
            address: str | None,
            age: int = 30,
        ):
        self.id = id
        self.name = name
        self.sex = sex
        self.contact_details = contact_details
        self.address = address
        self.age = age
    
    def asdict(self):
        return {
            "id": self.id,
            "name": self.name,
            "sex": self.sex,
            "contact_details": self.contact_details,
            "address": self.address,
            "age": self.age
        }
