"""
Weather API Routes

Defines endpoints for getting weather information
from SMHI SNOW REST API
"""

from fastapi import  APIRouter, Depends, Query
from app.models.weather import Weather

router = APIRouter(tags =["weather"])

@router.get("/weather")