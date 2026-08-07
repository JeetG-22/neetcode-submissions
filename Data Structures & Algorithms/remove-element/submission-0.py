class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered_list = []
        for i in range(len(nums)):
            if(val == nums[i]):
                continue
            filtered_list.append(nums[i]) 
        nums[:len(filtered_list)] = filtered_list
        return len(filtered_list)
        