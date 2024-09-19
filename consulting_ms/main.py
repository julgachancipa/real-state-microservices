from api.endpoints import re_property
from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

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
