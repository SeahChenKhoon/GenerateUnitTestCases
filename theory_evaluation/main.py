# Libraries required ======================
from . import config
from .evaluator import general_qa

import fastapi
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],  # This will output logs to the console
)
logger = logging.getLogger(__name__)

# SETTING UP FASTAPI APP ==========
APP = fastapi.FastAPI(title=config.SETTINGS.API_NAME)

ORIGINS = ["*"]
# allowed_origins = [
#     "http://localhost:3000",  # Local frontend server
#     "https://20.212.132.190.nip.io", # Production frontend
# ]

APP.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,  # allowed_origins
    allow_credentials=True,  # backend returns response to frontend requests even without authentication credentials - CORS has to allowed all origins.
    allow_methods=["*"],  # HTTP request methods - GET, POST, PUT, DELETE.
    allow_headers=[
        "*"
    ],  # to configure allowable headers to make request. e.g http://localhost:3000/[any_header]
)


# API for the evaluation llms ===============
APP.include_router(general_qa.router)


# API for health check ==============
@APP.get("/health")
def health_check():
    return JSONResponse(status_code=200, content={"status": "healthy"})


@APP.on_event("startup")
async def startup_event():
    logger.info("Starting up the FastAPI application")


@APP.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the FastAPI application")
