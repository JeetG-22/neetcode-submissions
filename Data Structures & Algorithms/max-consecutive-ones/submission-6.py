class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        for num in nums:
            if num != 1:
                max_ones = max(max_ones, count)
                count = 0
                continue
            count += 1
        return max(max_ones, count)



        