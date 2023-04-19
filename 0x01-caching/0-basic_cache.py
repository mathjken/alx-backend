#!/usr/bin/python3
from typing import Optional
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """BasicCache class"""
    
    def __init__(self):
        super().__init__()
        self.max_size = 1000 # maximum size of cache
        self.current_size = 0 # current size of cache
        self.head = None # head of cache
        self.tail = None # tail of cache
    
    def put(self, key: str, value: str) -> None:
        """Add a new key-value pair to the cache"""
        if key is None or value is None:
            return
        
        # remove the oldest item from cache if it has reached maximum size
        if self.current_size >= self.max_size and self.tail is not None:
            self.cache_data.pop(self.tail.key)
            self._move_to_front(self.tail)
            self.current_size -= 1
        
        # add new item to cache
        if key in self.cache_data:
            node = self.cache_data[key]
            node.value = value
            self._move_to_front(node)
        else:
            node = Node(key, value)
            self.cache_data[key] = node
            self._add_to_front(node)
            self.current_size += 1
        
    def get(self, key: str) -> Optional[str]:
        """Get the value associated with the given key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        
        # move the accessed item to the front of the cache
        node = self.cache_data[key]
        self._move_to_front(node)
        return node.value
    
    def _add_to_front(self, node: 'Node') -> None:
        """Add the given node to the front of the cache"""
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        
    def _move_to_front(self, node: 'Node') -> None:
        """Move the given node to the front of the cache"""
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        self._add_to_front(node)
        
class Node:
    """Node class for linked list"""
    
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

