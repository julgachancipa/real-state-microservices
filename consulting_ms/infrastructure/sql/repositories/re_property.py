from sqlalchemy import text

from infrastructure.sql.repositories.abstract import AbstractRepository
from settings import Settings

settings = Settings()


class REPropertyRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_filtering(self, year: int, city: str, status: list[str]):
        sql_query = """
            SELECT
                p.*,
                s.name AS status_name
            FROM property p
            JOIN (
                SELECT
                    sh.property_id,
                    sh.status_id
                FROM status_history sh
                JOIN (
                    SELECT property_id, MAX(update_date) AS latest_update
                    FROM status_history
                    GROUP BY property_id
                ) latest ON sh.property_id = latest.property_id AND sh.update_date = latest.latest_update
            ) most_recent ON p.id = most_recent.property_id
            JOIN status s ON most_recent.status_id = s.id
            WHERE 1=1
            """

        # Add filters based on parameters
        if year:
            sql_query += f" AND year = {year}"
        if city:
            sql_query += f" AND city = '{city}'"

        if not status:
            status = settings.VALID_STATUSES
        if len(status) == 1:
            sql_query += f" AND s.name = '{status[0]}'"
        else:
            sql_query += f" AND s.name IN {tuple(status)}"

        properties = self.session.execute(text(sql_query)).fetchall()
        return [dict(re_property._mapping) for re_property in properties]
