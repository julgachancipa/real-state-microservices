from api.schemas.re_property import REPropertySchema
from infrastructure.sql.repositories.re_property import REPropertyRepository


class REPropertyController:
    def __init__(self):
        self.re_property_repository = REPropertyRepository()

    # def get_filtering(self, re_property: REPropertySchema):
    def get_filtering(self):
        return self.re_property_repository.get_filtering()
