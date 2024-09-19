from fastapi import APIRouter

from api.schemas.re_property import REPropertySchema
from controllers.re_property import REPropertyController

router = APIRouter()


@router.get("/properties")
def get_properties():
    return REPropertyController().get_filtering()
