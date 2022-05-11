class SSIUOM:
    def __init__(
        self,
        id: str,
        meta_uom_name: str,
        uom_id: str | None = None
    ):
        self.id = id
        self.meta_uom_name = meta_uom_name
        self.uom_id = uom_id

    def asdict(self):
        return {
            "id": self.id,
            "meta_uom_name": self.meta_uom_name,
            "uom_id": self.uom_id
        }
