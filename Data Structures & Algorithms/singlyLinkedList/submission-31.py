class Node:
    def __init__(self, val=None, nextn=None):
        self.val = val
        self.nextn = nextn

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    
    def get(self, index: int) -> int:
        cur = self.head.nextn
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.nextn
            i+=1
        return -1

        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head.nextn:
            self.tail = new_node
        new_node.nextn = self.head.nextn
        self.head.nextn = new_node 

        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.nextn = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        prev, cur = self.head, self.head.nextn
        i = 0
        while cur:
            if i == index:
                if cur.nextn == None:
                    self.tail = prev
                    self.tail.nextn = None
                else:
                    prev.nextn = cur.nextn
                return True
            prev = cur
            cur = cur.nextn
            i += 1
        return False

        

    def getValues(self) -> List[int]:
        arr = []
        cur = self.head.nextn
        while cur:
            arr.append(cur.val)
            cur = cur.nextn
        return arr
        
