class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set() 
        j = 0
        for i in range(len(nums)):
            if nums[i] not in unique_set:
                unique_set.add(nums[i])
                nums[j] = nums[i]
                j += 1
        return len(unique_set) 

        