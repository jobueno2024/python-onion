from fastapi import APIRouter
from usecase.user_usecase import UserUseCase
from infrastructure.user_repository import UserRepository

router = APIRouter()

user_usecase = UserUseCase(UserRepository())

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_usecase.get_user(user_id)
    return user
