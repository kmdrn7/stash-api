from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/hello")
def api_v1_get_hello_world():
    return JSONResponse(
        status_code=200,
        content={
            "Status": "OK"
        }
    )
