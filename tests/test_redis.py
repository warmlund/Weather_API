"""
Unit tests for redis related functions

Tests:
- Cached weather data is returned when present in Redis.
- None is returned when no cached weather data exists.
- Cache keys are generated in the expected format.

"""
import json
from app.utils.redis import get_cached_weather, create_cache_key

class FakeRedis:
    def get(self, key):
        return json.dumps([
            {"time": "x", "temperature": 10}
        ])

class EmptyRedis:
    def get(self, key):
        return None

def test_get_cached_weather_miss():
    """
    Verify that None is returned when the cache contains no data
    for the requested weather key.
    """
    result = get_cached_weather(
        EmptyRedis(),
        "temperature:58:16"
    )

    assert result is None

def test_get_cached_weather():
    """
    Verify that cached weather data is deserialized and returned
    when a matching cache entry exists.
    """
    result = get_cached_weather(
        FakeRedis(),
        "temperature:58:16"
    )

    assert result == [
        {"time": "x", "temperature": 10}
    ]

def test_create_cache_key():
    """
    Verify that cache keys are generated using the expected
    temperature:<latitude>:<longitude> format.
    """
    assert create_cache_key(58.4, 16.2) == "temperature:58.4:16.2"
    