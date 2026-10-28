class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while(curr):
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head, self.head.next)
        #if there is no nodes in the ll we need to update tail 
        if not self.head.next:
            self.tail = new_node 
        else: #at least one node
            self.head.next.prev = new_node

        self.head.next = new_node
        self.length += 1 


        
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val, self.tail, None)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or self.length < index:
            return
        if self.length == index:
            self.addAtTail(val)
            return
        curr = self.head.next
        i = 0
        while(curr):
            if index == i:
                new_node = Node(val, curr.prev, curr)
                curr.prev.next = new_node
                curr.prev = new_node
            i += 1
            curr = curr.next
        self.length += 1


        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.length <= index:
            return
        curr = self.head.next
        i = 0 
        while(curr):
            if i == index:
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                curr.prev.next = curr.next
                self.length -= 1
                break
            i += 1
            curr = curr.next
        if not self.length:
            self.tail = self.head
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)