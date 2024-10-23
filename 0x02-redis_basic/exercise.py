#!/usr/bin/env python3
"""
This script creates a Cache class
"""

from typing import Union
import redis
import uuid


class Cache:
    """
    The __init__ method of the class stores a Redis client
    instance redis.Redis() as a private attribute called _redis

    - store: A Method of the Cache class.
    """
    def __init__(self):
        """Inititalizing a Redis client"""
        self._redis = redis.Redis()
        # clearing any existing Redis data
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """storing the data using a generated random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key
