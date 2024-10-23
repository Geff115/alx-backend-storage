#!/usr/bin/env python3
"""
This script creates a Cache class
"""

from typing import Union, Callable
import redis
import uuid


class Cache:
    """
    The __init__ method of the class stores a Redis client
    instance redis.Redis() as a private attribute called _redis

    - store: A Method of the Cache class.
    """
    def __init__(self) -> None:
        """Inititalizing a Redis client"""
        self._redis = redis.Redis()
        # clearing any existing Redis data
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """storing the data using a generated random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, None]:
        """Retrieves data from the Redis cache using the given key.
        ARGS:
            key: The key used to retrieve the data.
            fn: An optional callable function that will be
            applied to the retrieved data before returning.
        RETURN:
            The retrieved data, or None if the key is not found.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, None]:
        """This method decodes the byte string to a
        UTF-8 string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """This method converts the byte string to an
        integer
        """
        return self.get(key, int)
