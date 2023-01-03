from typing import Optional
from src.adapters.database.postgres.engine import get_db
from src.adapters.database.postgres.user import UserSchema
from src.core.domain.user.database_interface import UserDatabaseInterface

class UserAdapter(UserDatabaseInterface):

    def create(self, name: str, email: str, password: str) -> UserSchema:
        db_user = UserSchema(
            name = name,
            email = email,
            password = password
        )
        self.database.add(db_user)
        self.database.commit()
        self.database.refresh(db_user)
        return db_user

    def list(self, text_search: Optional[str] = None,
                    page: Optional[str] = 1) -> list[UserSchema]:
        return [user.to_dict() for user in self.database.query(UserSchema).all() ]
    
    def get(self, user_id: int) -> UserSchema:
        return self.database.query(UserSchema).filter(UserSchema.id == user_id).first()
    
    def delete(self, user_id: int) -> bool:
        self.database.query(UserSchema).filter(UserSchema.id == user_id).delete()
        self.database.commit()
        return True