from src.core.domain.user.service import UserAdapter
from src.datalayer.database.postgres.user import UserDatabaseRepository

def make_user_controller():
    repository = UserDatabaseRepository()
    return UserAdapter(repository)