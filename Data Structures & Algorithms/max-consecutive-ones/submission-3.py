class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp_count, count = 0, 0

        for num in nums:
            if num == 1:
                temp_count += 1
            else:
                count = max(count, temp_count)
                temp_count = 0
        return max(count,temp_count)

        