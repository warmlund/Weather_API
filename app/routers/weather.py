"""
Weather API Routes

Defines endpoints for getting weather information
from SMHI SNOW REST API
"""

from fastapi import  APIRouter, Depends, HTTPException
from app.models.weather import WeatherResponse
from app.utils.redis import get_redis, create_cache_key, get_cached_weather
from upstash_redis import Redis
import os
import json
import httpx
from dotenv import load_dotenv
from app.utils.weather_utils import extract_temperature

load_dotenv()
router = APIRouter(tags =["weather"])
BASE_URL = os.getenv("BASEURL")

@router.get("/weather", response_model= list[WeatherResponse], status_code=200)
async def get_weather(lat: float, long: float, redis: Redis = Depends(get_redis)):
    """
    Gets air temperature for at certain corrdinate point

    Args:
       lat: latitude
       long: longitude
       redis: redis cache database

    Returns:
        HTTP 200 successul request

    Raises:
        HTTP 400 if the input coordinate is out of bounds
        HTTP 404 if data is not found
    """
    
    cache_key = create_cache_key(lat, long)
    get_cached_weather(redis, cache_key)
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/geotype/point/lon/{long}/lat/{lat}/data.json")
            response.raise_for_status()
    
    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=400,
            detail="Field point is out of bounds"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=404,
            detail="Weather data not found"
        )
    
    weather_data = response.json()
    temperatures = extract_temperature(weather_data)

    redis.setex(
        cache_key, 600, json.dumps(temperatures)
        )

    return temperatures