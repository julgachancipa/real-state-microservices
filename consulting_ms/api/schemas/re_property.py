from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel, Field


class QueryParams(BaseModel):
    year: Optional[int] = Query(default=None)
    city: Optional[str] = Query(default=None)
    status_list: List[str] = Field(Query(default=[]))


class REPropertySchema(BaseModel):
    address: str
    city: str
    status_name: str
    price: int
    description: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "address": "carrera 100 #15-90",
                    "city": "bogota",
                    "status_name": "en_venta",
                    "price": 350000000,
                    "description": "Amplio apartamento en conjunto cerrado",
                }
            ]
        }
    }


class IncompleteREPropertySchema(BaseModel):
    address: Optional[str]
    city: Optional[str]
    status_name: Optional[str]
    price: Optional[int]
    description: Optional[str]


class MultiStatusResponse(BaseModel):
    detail: List
    body: List[IncompleteREPropertySchema]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "detail": [
                        {
                            "type": "string_type",
                            "loc": ["response", 0, "description"],
                            "msg": "Input should be a valid string",
                            "input": None,
                        },
                        {
                            "type": "string_type",
                            "loc": ["response", 1, "description"],
                            "msg": "Input should be a valid string",
                            "input": None,
                        },
                    ],
                    "body": [
                        {
                            "address": "calle 18 k 43 - 12e",
                            "city": "cali",
                            "status_name": "pre_venta",
                            "price": 125000000,
                            "description": None,
                        },
                        {
                            "address": "calle 18 k 43",
                            "city": "cali",
                            "status_name": "pre_venta",
                            "price": 125000000,
                            "description": None,
                        },
                    ],
                }
            ]
        }
    }
