from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.controllers import core_entry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    app = FastAPI(lifespan=lifespan)
    app.include_router(core_entry.router)
    uvicorn.run(app, host="0.0.0.0", port=8000)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialization (Startup)
    logger.info("Cognitive CORE - Initializing...")

    yield

logger.info("Cognitive CORE - Shutting down...")


if __name__ == "__main__":
    main()

