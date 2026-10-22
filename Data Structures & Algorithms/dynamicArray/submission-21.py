class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == len(self.arr):
            self.resize()
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        self.length -= 1
        ele = self.arr[self.length]
        return ele
 

    def resize(self) -> None:
        new_arr = [0] * len(self.arr) * 2 
        for i, ele in enumerate(self.arr):
            new_arr[i] = ele
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length

        
    def getCapacity(self) -> int:
        return len(self.arr)
