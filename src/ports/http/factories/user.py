from src.core.domain.user.service import UserService
from src.repository.sqlalchemy.user import UserDatabaseRepository

def make_user_controller():
    repository = UserDatabaseRepository()
    return UserService(repository)