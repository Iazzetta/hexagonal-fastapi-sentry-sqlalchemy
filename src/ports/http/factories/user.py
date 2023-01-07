from src.core.domain.user.service import UserService
from src.adapters.database.postgres.user import UserDatabaseRepository

def make_user_controller():
    repository = UserDatabaseRepository()
    return UserService(repository)