from src.domain.user import User
from src.infrastructure.user_repository import UserRepository

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id)
