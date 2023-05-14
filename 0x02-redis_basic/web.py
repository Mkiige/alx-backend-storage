import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=10)  # Cache with maxsize of 100 and expiration time of 10 seconds

@cached(cache)
def get_page(url: str) -> str:
    """Retrieve HTML content of a webpage and cache the result for 10 seconds."""
    response = requests.get(url)
    return response.content.decode('utf-8')
