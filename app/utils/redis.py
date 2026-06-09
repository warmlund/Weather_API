"""
Redis configuration

Functions:
    Initializes the rdis database for caching
    Creates cache key
"""

import json
from fastapi import Request

def get_redis(request:Request):
    return request.app.state.redis

def create_cache_key(lat: float, long: float) -> str:
    return f"temperature:{lat}:{long}"

def get_cached_weather(redis, cache_key):
    cached = redis.get(cache_key)

    if cached:
        return json.loads(cached)

    return None