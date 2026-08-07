class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i // 2



    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
    
        val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)

        return val


    def percolate_down(self, start):
        i = start
        while i * 2 < len(self.heap):
            left = i * 2
            right = i * 2 + 1
            smallest = i
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if self.heap[left] < self.heap[smallest]:
                smallest = left
            if smallest == i:
                break
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest] 
            i = smallest

        

    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return
        nums.append(nums[0])
        self.heap = nums 
        curr = (len(self.heap) - 1) // 2
        while curr >= 1:
            i = curr
            self.percolate_down(i)
            curr -= 1

        
        