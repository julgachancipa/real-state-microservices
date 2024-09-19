from infrastructure.sql.connection import Connection


class AbstractRepository:
    def __init__(self) -> None:
        self.connection = Connection()
        self.session = self.connection.session
