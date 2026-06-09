from contextlib import asynccontextmanager
from fastapi import FastAPI
from upstash_redis import Redis
from app.routers.weather import router as weather_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan handler

    runs on startup connecting to Redis for caching weather data
    using environment variables
    """

    app.state.redis = Redis.from_env()
    yield

def create_app() -> FastAPI:
    """
    FastAPI entry point

    Intializes the application and API routes
    """

    app = FastAPI(lifespan = lifespan)
    app.include_router(weather_router)

    return app

app = create_app()