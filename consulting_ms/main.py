import uvicorn
from fastapi import APIRouter, FastAPI, Response
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from api.endpoints import re_property
from api.schemas.re_property import MultiStatusResponse

app = FastAPI(title="Habi: Consulting properties API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ResponseValidationError)
def validation_exception_handler(response: Response, exc: ResponseValidationError):
    response_data = MultiStatusResponse(
        detail=exc.errors(),
        body=exc.body,
    )

    return JSONResponse(
        status_code=207,
        content=response_data.model_dump(),
    )


router = APIRouter()

router.include_router(re_property.router, tags=["properties"])

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app)
