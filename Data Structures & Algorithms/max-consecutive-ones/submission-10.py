class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            count = count + 1 if num == 1 else 0
            max_count = max(count, max_count)
        return max_count


        