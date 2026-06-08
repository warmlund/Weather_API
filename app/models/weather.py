"""
Weather models

Defines models for the Weather data retrieved from SMHI SNOW
- Base model with location, time and temperature
"""

from pydantic import BaseModel

class Weather(BaseModel):
    """
    Base model for a Weather item
    """
    id: int
    coordinate: list[float]
    time: str
    temperature: float