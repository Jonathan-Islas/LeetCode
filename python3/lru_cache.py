# LRU Cache

# Requirements:
# Cache has positive capacity
# get(key) -> return cache[key] if exists, else return -1
# put(key,value) -> * If this operation overflows capacity: remove LRU key and then put new key:value
#                   * else, add new key:value

# get and put runtime complextity = O(1)
# keep track of LRU key

# Key Usage Order:
# K4 Most recent - TAIL
# K3
# K1
# K2
# K5 Least recent - HEAD

# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# dictionary for storage of key:value pairs -> OK
# ADD, DELETE, UPDATE, CHECK IF KEY EXISTS = O(1)

# LRU tracking: Doubly Linked List -> INSERTION & DELETION = O(1)

class CacheNode:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        
        # dummy head and tail
        self._head = CacheNode(-1,-1) # Before LRU
        self._tail = CacheNode(-1,-1) # After MRU
        
        self._head.next = self._tail
        self._tail.prev = self._head


    def get(self, key: int) -> int:
        # if key does not exist, return -1
        if key not in self._cache:
            return -1
        
        # if exists, get node mapped to key
        node = self._cache[key]
        
        # update LRU keys order
        self._remove(node) # remove node reference
        self._add(node) # add node to end
        
        return node.value


    def put(self, key: int, value: int) -> None:
        # if key exists
        if key in self._cache:
            node = self._cache[key]
            del self._cache[key]
            # remove node reference mapped to existing key
            self._remove(node)
        
        # if this operation exceeds capacity, delete LRU key
        if len(self._cache) == self._capacity:
            # remove from cache dict
            del self._cache[self._head.next.key]
            # remove node reference
            self._remove(self._head.next)
            
        # add to cache dict
        self._cache[key] = CacheNode(key,value)
        # update LRU keys order by adding node
        self._add(self._cache[key])
        
        
    # Function to remove node
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    
    # Functio to add node
    def _add(self, node):
        # get current end node
        current_end = self._tail.prev
        current_end.next = node
        
        node.prev = current_end
        node.next = self._tail
        
        self._tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)# lru_cache.py
