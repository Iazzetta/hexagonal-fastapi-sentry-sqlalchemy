from src.core.domain.user.service import UserAdapter
from sqlalchemy.orm import Session
from src.datalayer.database.postgres.engine import get_db

def make_user_controller():
    database: Session = next(get_db())
    return UserAdapter(database)