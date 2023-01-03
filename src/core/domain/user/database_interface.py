from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from sqlalchemy.orm import Session
from src.datalayer.database.postgres.engine import get_db
from src.core.domain.user.user import User

@dataclass
class UserDatabaseInterface(ABC):

    database: Session = next(get_db())

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