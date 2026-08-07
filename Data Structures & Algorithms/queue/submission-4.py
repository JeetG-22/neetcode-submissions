class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def isEmpty(self) -> bool:
        if self.head.next:
            return False
        return True
        

    def append(self, value: int) -> None:
        newNode = Node(value, None, self.tail)
        self.tail.next = newNode
        self.tail = newNode
        

    def appendleft(self, value: int) -> None:
        newNode = Node(value, self.head.next, self.head)
        if self.isEmpty():
            self.tail = newNode
        else:
            self.head.next.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.head.next.data 
        self.head.next = self.head.next.next
        if self.head.next:
            self.head.next.prev = self.head
        else:
            self.tail = self.head
        return val
        


class Node:
    def __init__(self, data=-1, next=None, prev=None):
        self.next = next
        self.data = data
        self.prev = prev

        
