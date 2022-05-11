class BillItem:
    def __init__(
            self,
            id: str,
            meta_name: str,
            meta_price: float = 0.0,
            meta_quantity: int = 1,
            meta_subtotal: float = 0.0,
            ss_id: str | None = None,
        ):
        self.id = id
        self.meta_name = meta_name
        self.meta_price = meta_price
        self.meta_quantity = meta_quantity
        self.meta_subtotal = meta_subtotal
        self.ss_id = ss_id

    def _calculate_subtotal(self):
        self.meta_subtotal = self.meta_quantity * self.meta_price

    def modify_quantity(self, qty: int):
        self.meta_quantity = qty
        self._calculate_subtotal()

    def get_meta_subtotal(self):
        return self.meta_subtotal

    def asdict(self):
        return {
            "id": self.id,
            "meta_name": self.meta_name,
            "meta_price": self.meta_price,
            "meta_quantity": self.meta_quantity,
            "meta_subtotal": self.meta_subtotal,
            "ss_id": self.ss_id
        }
