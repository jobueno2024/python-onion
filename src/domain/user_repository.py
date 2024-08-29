from abc import ABC, abstractmethod
from typing import List
from domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[User]:
        raise NotImplementedError
