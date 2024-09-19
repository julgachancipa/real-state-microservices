from infrastructure.sql.instance_converter import ORMInstanceConverter
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func


class BaseModel:
    """The BaseModel class from which futures classes will be derived"""

    id = Column(Integer, primary_key=True)

    def to_dict(self) -> dict:
        """
        Converts an ORM instance into a dictionary.
        """
        return ORMInstanceConverter().convert_to_dict(self)
