class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == len(self.arr):
            self.resize()
        self.arr[self.capacity] = n
        self.capacity += 1

    def popback(self) -> int:
        if self.capacity > 0:
            self.capacity -= 1
        return self.arr[self.capacity]
    def resize(self) -> None:
        # Create new array of double capacity
        new_arr = [0] * (2 * len(self.arr))
        
        # Copy elements to new_arr
        for i in range(self.capacity):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.capacity
    
    def getCapacity(self) -> int:
        return len(self.arr)


