#!/usr/bin/python3
"""FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class
    Args:
        BaseCaching (class): Basic class for this class
    """

    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """Add a new key-value pair to the cache dictionary and the list
        of keys using the FIFO algorithm. If the maximum number of items
        is reached, remove the oldest item from the dictionary and the list
        of keys.
        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discd = self.__keys.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discd))
        if key and item:
            self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get the value associated with the given key from the cache
        dictionary, or None if the key is not in the dictionary.
        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
