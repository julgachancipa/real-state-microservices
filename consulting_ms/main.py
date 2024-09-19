import uvicorn
from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.endpoints import re_property

app = FastAPI(title="Habi: Consulting properties API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

router.include_router(re_property.router, tags=["properties"])

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app)
