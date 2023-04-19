#!/usr/bin/python3
"""BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A simple cache that stores key-value pairs in a dictionary
    Args:
        BaseCaching (class): Basic class for this class
    """

    def put(self, key, item):
        """Add a new key-value pair to the cache dictionary
        Args:
            key ([type]): key of dictionary self.cache_data
            item ([type]): value of key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key from the cache dictionary
        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
