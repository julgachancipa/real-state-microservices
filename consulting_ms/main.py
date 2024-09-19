from api.endpoints import properties
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

router.include_router(properties.router, tags=["properties"])

app.include_router(router)
