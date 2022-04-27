#!/usr/bin/env python3
"""Module for tracking url """
import redis
import requests
redi = redis.Redis()
counter = 0


def get_page(url: str) -> str:
    """track how many times a particular URL
    was accessed in the key""" 
    redi.set(f"cached:{url}", counter)
    resp = requests.get(url)
    redi.incr(f"count:{url}")
    redi.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
