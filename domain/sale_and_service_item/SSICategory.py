class SSICategory:
    def __init__(
            self,
            id: str,
            meta_category_name: str,
            category_id: str
        ):
        self.id = id
        self.meta_category_name = meta_category_name
        self.category_id = category_id

    def asdict(self):
        return {
            "id": self.id,
            "meta_category_name": self.meta_category_name,
            "category_id": self.category_id
        }
