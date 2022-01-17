from fastapi import APIRouter
from app.http.api.v1 import hello_world

router = APIRouter()
router.prefix = "/api/v1"
router.include_in_schema = False

router.include_router(hello_world.router)
