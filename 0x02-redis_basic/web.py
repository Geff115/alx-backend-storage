#!/usr/bin/env python3
"""
This script fetches HTML content of a URL and caches it.
"""

import requests
import redis
import functools
from typing import Callable


# Initialize Redis client
r = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """Decorator to cache page results and track access count."""
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function"""
        count_key = f"count:{url}"
        cached_page = r.get(url)

        if cached_page:
            # If cache exists, increment the count and return cached result
            r.incr(count_key)
            return cached_page.decode("utf-8")

        # If cache does not exist, call the original method to fetch the page
        result = method(url)

        # Cache the result with an expiration of 10 seconds
        r.setex(url, 10, result)

        # Increment the access count
        r.incr(count_key)

        return result

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL."""
    response = requests.get(url)
    return response.text
