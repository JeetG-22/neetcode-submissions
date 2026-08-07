class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next_node
        count = 0
        while cur:
            if count == index:
                return cur.val 
            count += 1
            cur = cur.next_node
        return -1
        

    def insertHead(self, val: int) -> None:
        temp = Node(val)
        temp.next_node = self.head.next_node
        self.head.next_node = temp
        if self.head == self.tail:
            self.tail = temp
        

    def insertTail(self, val: int) -> None:
        temp = Node(val)
        self.tail.next_node = temp
        self.tail = temp

    def remove(self, index: int) -> bool:
        count = 0 
        cur = self.head
        while cur and count < index:
            count += 1
            cur = cur.next_node
        if cur and cur.next_node:
            cur.next_node = cur.next_node.next_node 
            if not cur.next_node: #change tail
                self.tail = cur
            return True
        return False
        
    def getValues(self) -> List[int]:
        values = []
        cur = self.head.next_node
        while cur:
            values.append(cur.val)
            cur = cur.next_node
        return values
        
