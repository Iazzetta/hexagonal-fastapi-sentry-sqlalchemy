from dataclasses import dataclass
from typing import Optional
from src.datalayer.database.postgres.schemas.user import UserSchema
from src.datalayer.database.postgres.user import UserDatabaseRepository

@dataclass
class UserService():

    __user_repository: UserDatabaseRepository

    def create(self, name: str, email: str, password: str) -> UserSchema:

        new_user = self.__user_repository.create(name, email, password)
        return new_user

    def list(self, text_search: Optional[str] = None,
                    page: Optional[str] = 1) -> list[UserSchema]:

        list_users = self.__user_repository.list(text_search, page)
        return list_users
    
    def get(self, user_id: int) -> UserSchema:

        user = self.__user_repository.get(user_id)
        return user
    
    def delete(self, user_id: int) -> bool:
        
        deleted = self.__user_repository.delete(user_id)
        return deleted