from domain.sale_and_service_item.SSICategory import SSICategory
from domain.sale_and_service_item.SSIUOM import SSIUOM

class SaleAndServiceItem:
    def __init__(
       self,
       name: str,
       ssi_uoms: list[SSIUOM] = [],
       ssi_categories: list[SSICategory] = [],
       price: float = 0.0,
       ):
        self.name = name
        self.ssi_uoms = ssi_uoms
        self.ssi_categories = ssi_categories
        self.price = price

    def modify_sale_and_service_item(
            self,
            name: str,
            ssi_uom: SSIUOM,
            ssi_categories: list[SSICategory],
            price: float = 0.0,
        ):
        self.name = name
        self.ssi_uom = ssi_uom
        self.ssi_categories = ssi_categories
        self.price = price

    def add_uom(self, uom: SSIUOM):
        self.ssi_uoms.append(uom)

    def remove_uom(self, index: int):
        if index >= 0 and index < len(self.ssi_uoms):
            self.ssi_uoms.pop(index)

    def add_category(self, category: SSICategory):
        self.ssi_categories.append(category)

    def remove_category(self, index: int):
        if index >= 0 and index < len(self.ssi_categories):
            self.ssi_categories.pop(index)

    def asdict(self):
        return {
            "name": self.name,
            "ssi_uom": [uom.asdict() for uom in self.ssi_uoms],
            "ssi_categories": [category.asdict() for category in self.ssi_categories],
            "price": self.price
        }
