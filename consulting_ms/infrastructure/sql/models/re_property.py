from infrastructure.sql.models.base import Base
from infrastructure.sql.models.base_model import BaseModel
from infrastructure.sql.models.user import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class REProperty(BaseModel, Base):
    __tablename__ = "re_property"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String)
    city = Column(String)
    price = Column(BigInteger)
    description = Column(Text)
    year = Column(Integer)
