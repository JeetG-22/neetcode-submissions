class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Remove it from current position
        self.remove(node)
        # Insert at front (most recently used)
        self.insert(node)
        return node.val  # Return node.val directly

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # Insert right after left dummy (most recently used position)
        node.prev = self.left
        node.next = self.left.next 
        self.left.next.prev = node
        self.left.next = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value  # Update the existing node's value
            self.insert(node)
            return
        
        # Check capacity BEFORE adding (>= not >)
        if len(self.cache) >= self.capacity:
            # Remove LRU node (right before right dummy)
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]  # FIX: Use lru.key, not key!
        
        # Create new node and add to both structures
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)  # FIX: Insert the SAME node object!