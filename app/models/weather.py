"""
Weather models

Defines models for the Weather data retrieved from SMHI SNOW
- Base model with location, time and temperature
"""

from pydantic import BaseModel

class WeatherRequest(BaseModel):
    """
    Base model for weather request item
    """
    latitude: float
    longitude: float



class WeatherResponse(BaseModel):
    """
    Base model for a Weather response item
    """
    time: str
    temperature: float