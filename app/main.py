from fastapi import FastAPI
from app.routers.weather import router as weather_router

def create_app() -> FastAPI:
    """
    FastAPI entry point

    Intializes the application and API routes
    """

    app = FastAPI()
    app.include_router(weather_router)

    return app

app = create_app()