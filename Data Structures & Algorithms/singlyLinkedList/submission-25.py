class LinkedList:
    
    def __init__(self):
        self.head = Node("temp")
        self.tail = self.head 

    
    def get(self, index: int) -> int:
        i = 0
        temp = self.head.next_node
        while temp:
            if i == index:
                return temp.data
            i += 1
            temp = temp.next_node

        return -1
        

    def insertHead(self, val: int) -> None:
        newNode = Node(val, self.head.next_node)
        if not self.head.next_node:
           self.tail = newNode 
        self.head.next_node = newNode

        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next_node = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        i = 0
        temp = self.head
        while i < index and temp:
            i += 1
            temp = temp.next_node
        
        if temp and temp.next_node:
            if temp.next_node == self.tail:
                self.tail = temp
            temp.next_node = temp.next_node.next_node
            return True
        return False
            
        return False

        

    def getValues(self) -> List[int]:
        ll_list = []
        temp = self.head.next_node
        while temp:
            ll_list.append(temp.data)
            temp = temp.next_node
        return ll_list
        
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
