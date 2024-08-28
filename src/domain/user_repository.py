from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        raise NotImplementedError
