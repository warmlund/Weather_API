"""
Redis configuration

Initializes the rdis database for caching
"""

from fastapi import Request

def get_redis(request:Request):
    return request.app.state.redis