from fastapi import APIRouter, status, Depends
from infrastructure.schemas.category import Category as CategoryDTO
from infrastructure.repositories.category import CategoryRepository
from usecases.category import CategoryUseCase

router = APIRouter(prefix="/categories", tags=["Categories"]) 

@router.post("createCategory", status_code=status.HTTP_200_OK, response_model=CategoryDTO)
def create_patient(request: CategoryDTO, repo=Depends(CategoryRepository)):
    return CategoryUseCase(repo).create_category(request)

