from typing import List

from domain.user import User
from domain.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):
    def get_user_by_id(self, user_id: int) -> User:
        # ここでは仮のデータを返しますが、実際にはデータベースから取得します
        return User(id=user_id, name="John Doe", email="john.doe@example.com")

    def find_all(self) -> List[User]:
        users = [
            User(id=1, name="John Doe", email="john.doe@example.com")
            , User(id=2, name="John Doe", email="john.doe@example.com")
        ]
        return users
