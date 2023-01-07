from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from src.core.domain.user.user import User

@dataclass
class UserDatabaseInterface(ABC):

    @abstractmethod
    def create(self, name: str, email: str, password: str) -> User:
        pass
    
    @abstractmethod
    def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    def list(self, text_search: Optional[str] = None,
                    page: Optional[str] = 1) -> list[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass