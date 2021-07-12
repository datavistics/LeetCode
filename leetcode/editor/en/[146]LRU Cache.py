# Design a data structure that follows the constraints of a Least Recently Used 
# (LRU) cache. 
# 
#  Implement the LRUCache class: 
# 
#  
#  LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 
# 
#  int get(int key) Return the value of the key if the key exists, otherwise ret
# urn -1. 
#  void put(int key, int value) Update the value of the key if the key exists. O
# therwise, add the key-value pair to the cache. If the number of keys exceeds the
#  capacity from this operation, evict the least recently used key. 
#  
# 
#  The functions get and put must each run in O(1) average time complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 104 
#  0 <= value <= 105 
#  At most 2 * 105 calls will be made to get and put. 
#  
#  Related Topics Hash Table Linked List Design Doubly-Linked List 
#  👍 9131 👎 361


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, next=None, prev=None, val=None, key=None):
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.vals = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # Check if key exists
        if key in self.vals:
            n = self.vals[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        # Removal setup
        if key in self.vals:
            self.remove(self.vals[key])
        self.vals[key] = Node(val=value, key=key)
        self.add(self.vals[key])
        if len(self.vals) > self.capacity:
            del self.vals[self.head.next.key]
            self.remove(self.head.next)

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)

lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(2, 2)
lRUCache.get(2)
lRUCache.put(1, 1)
lRUCache.put(4, 1)
lRUCache.get(2)
pass

# Success:
# Runtime: 1160 ms, faster than 10.61% of Python3 online submissions.
# Memory Usage: 74.3 MB, less than 24.92% of Python3 online submissions.
