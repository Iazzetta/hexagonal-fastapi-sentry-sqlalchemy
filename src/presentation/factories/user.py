from src.core.domain.user.service import UserAdapter
from sqlalchemy.orm import Session
from src.datalayer.database.postgres.engine import get_db
from src.datalayer.database.postgres.user import UserDatabaseRepository

def make_user_controller():
    repository = UserDatabaseRepository()
    return UserAdapter(repository)