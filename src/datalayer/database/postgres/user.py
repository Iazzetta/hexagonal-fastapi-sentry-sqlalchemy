from sqlalchemy import Column, Integer, String
from src.datalayer.database.postgres.engine import Base

class UserSchema(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(120))
    password = Column(String(120))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }