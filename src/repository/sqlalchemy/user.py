from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm import Session
from src.repository.sqlalchemy.engine import get_db
from src.repository.sqlalchemy.schemas.user import UserSchema
from src.adapters.database.user import UserDatabaseInterface

@dataclass
class UserDatabaseRepository(UserDatabaseInterface):

    __database: Session = next(get_db())

    def create(self, name: str, email: str, password: str) -> UserSchema:
        db_user = UserSchema(
            name = name,
            email = email,
            password = password
        )
        self.__database.add(db_user)
        self.__database.commit()
        self.__database.refresh(db_user)
        return db_user

    # TODO - filter and pagination
    def list(self, text_search: Optional[str] = None,
                    page: Optional[str] = 1) -> list[UserSchema]:
        return [user.to_dict() for user in self.__database.query(UserSchema).all() ]
    
    def get(self, user_id: int) -> UserSchema:
        return self.__database.query(UserSchema).filter(UserSchema.id == user_id).first()
    
    def delete(self, user_id: int) -> bool:
        self.__database.query(UserSchema).filter(UserSchema.id == user_id).delete()
        self.__database.commit()
        return True