#!/usr/bin/env python3
"""Module store Redis"""
import redis
from import Union, Callable, Optional, Any


class Cache:
    """Class of cache """
    def __int___():
        """constructor store an instance of the redis"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random id
        Union[str, bytes, int, float]) -> str:"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
