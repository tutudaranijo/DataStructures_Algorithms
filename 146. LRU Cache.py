
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None  # both pointer are initializes 0


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key to nodes

        # * left = LRU and right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # helper functions
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # helper function, insert node at the right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # * remove if key in cache
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove and delete the lru form the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
