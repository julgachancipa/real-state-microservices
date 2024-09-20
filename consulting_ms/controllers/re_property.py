from fastapi import HTTPException

from api.schemas.re_property import REPropertySchema
from infrastructure.sql.repositories.re_property import REPropertyRepository
from settings import Settings

settings = Settings()


class REPropertyController:
    def __init__(self):
        self.re_property_repository = REPropertyRepository()

    # def get_filtering(self, re_property: REPropertySchema):
    def get_filtering(self, year: int, city: str, status_list: list[str]):
        # Validate the status parameter
        if status_list:
            for status in status_list:
                if status not in settings.VALID_STATUSES:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Invalid status value. Valid options are: {settings.VALID_STATUSES}",
                    )

        return self.re_property_repository.get_filtering(year, city, status_list)
