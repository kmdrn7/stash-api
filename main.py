from distutils.command.config import config
from fastapi import FastAPI
from app.core.config import settings
from app.http.middleware.add_process_time import AddProcessTimeHeader
from app.routes.base import health_check
from app.routes.api import api_v1

# Init config
conf = settings.setup()

# Init FastAPI instance
app = FastAPI(
    title=conf["APP_NAME"],
    openapi_url=conf["OPENAPI_URL"],
    version=conf["APP_VERSION"],
    redoc_url=None  # disable redocs, only use swagger
)

# Add Middlewares
app.add_middleware(AddProcessTimeHeader)

# Add Routes
app.include_router(health_check.router)
app.include_router(api_v1.router)
