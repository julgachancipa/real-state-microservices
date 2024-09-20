from typing import List, Union

from fastapi import APIRouter, Depends

from api.schemas.re_property import MultiStatusResponse, QueryParams, REPropertySchema
from controllers.re_property import REPropertyController

router = APIRouter()


@router.get(
    "/properties",
    response_model=List[REPropertySchema],
    responses={
        207: {
            "description": "Multi-Status Response, some properties have missing data",
            "model": MultiStatusResponse,
        },
        400: {
            "description": "Bad Request, invalid input information",
            "content": {"application/json": {"example": {"detail": "Invalid input"}}},
        },
    },
)
def get_properties(query: QueryParams = Depends()):
    return REPropertyController().get_filtering(
        query.year, query.city, query.status_list
    )


@router.get("/status")
def get_status():
    return {"status": "ok"}
