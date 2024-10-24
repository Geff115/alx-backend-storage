#!/usr/bin/env python3
"""
This script creates a Cache class
"""

from typing import Union, Callable, Any
import redis
import uuid
import functools


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs of a method."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """The wrapped function that stores the input/output history."""
        r = self._redis  # Access Redis client from the Cache instance

        # Defining keys for input and output lists
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Storing input arguments
        r.rpush(input_key, str(args))

        # Calling the original method and capturing its output
        result = method(self, *args, **kwargs)

        # Storing the output
        r.rpush(output_key, str(result))

        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    """This decorator takes a callable method as
    argument, and returns a Callable
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """The callable function"""
        r = self._redis  # Using the Redis client from the Cache instance

        # Generating the key for this function
        key = f"call_count:{method.__qualname__}"

        # Increment the counter
        r.incr(key)

        # Calling the original function
        result = method(self, *args, **kwargs)

        return result

    return wrapper


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

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
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
        # If the key is asking for the call count, return it
        if key == "Cache.store":
            count_key = f"call_count:{key}"
            count = self._redis.get(count_key)
            return count

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
