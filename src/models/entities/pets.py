from sqlalchemy import Column, BIGINT, String
from ..settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"PetsTable [name={self.name}, type={self.type}]"
