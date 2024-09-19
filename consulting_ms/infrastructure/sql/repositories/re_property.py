from sqlalchemy import text

from infrastructure.sql.repositories.abstract import AbstractRepository


class REPropertyRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_filtering(self):
        instances = self.session.execute(text("SELECT * FROM property")).fetchall()
        return [dict(instance._mapping) for instance in instances]
