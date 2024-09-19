from datetime import datetime

from pydantic import BaseModel, Field


class REPropertySchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    content: str = Field(..., min_length=1, max_length=200)
    created_at: str = Field(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user_id: int
