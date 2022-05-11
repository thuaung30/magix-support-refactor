from infrastructure.repositories.category import CategoryRepository
from infrastructure.schemas.category import Category as CategoryDTO;

class CategoryUseCase:
    def __init__(self, repo: CategoryRepository):
        self._repo = repo

    def create_category(self, category: CategoryDTO) -> CategoryDTO:
        return self._repo.create_category(category)
