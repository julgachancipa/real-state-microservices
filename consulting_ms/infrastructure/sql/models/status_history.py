from infrastructure.sql.models.base import Base
from infrastructure.sql.models.base_model import BaseModel
from infrastructure.sql.models.user import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class StatusHistory(BaseModel, Base):
    __tablename__ = "status_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    re_property_id = Column(Integer)
    update_date = Column(DateTime)

    status_id = Column(Integer, ForeignKey("property.id"))
    re_property = relationship("REProperty", back_populates="property")
