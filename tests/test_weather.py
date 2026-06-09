""""
Unit tests for weather related functions

Tests:
    - Test extraaction of temperature
    - Test that empty temperature extraction returns empty list
"""

from app.utils.weather_utils import extract_temperature

def test_extract_temperatures():
    """
    tests that temperature is extracted correctly

    """
    weather_data = {
        "timeSeries": [
            {
                "time": "2026-06-09T10:00:00Z",
                "data": {
                    "air_temperature": 13.7
                }
            }
        ]
    }

    result = extract_temperature(weather_data)

    assert result == [
        {
            "time": "2026-06-09T10:00:00Z",
            "air_temperature": 13.7
        }
    ]

def test_extract_temperatures_empty():
    """
    Extraction of empty list returns empty
    """
    weather_data = {
        "timeSeries": []
    }

    result = extract_temperature(weather_data)

    assert result == []

