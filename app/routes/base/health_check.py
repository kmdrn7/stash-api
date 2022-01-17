from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from loguru import logger

router = APIRouter()


@router.get("/healthz")
def get_healthz():
    logger.info("running health check :D")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"I'm": {"fine": {"Thanks": {"for": {"asking": ":D"}}}}}
    )
