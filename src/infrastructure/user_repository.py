from domain.user import User
from domain.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):
    def get_user_by_id(self, user_id: int) -> User:
        # ここでは仮のデータを返しますが、実際にはデータベースから取得します
        return User(id=user_id, name="John Doe", email="john.doe@example.com")
