class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_zeroes = 0
        for num in nums:
            if num == 0:
                num_zeroes += 1
                continue
            product *= num
        if num_zeroes > 1:
            return [0] * len(nums)
        output = [product] * len(nums)
        for i in range(len(nums)):
            if num_zeroes == 1 and nums[i] != 0:
                output[i] = 0
            elif num_zeroes == 0:
                output[i] //= nums[i]
            


                


            
        return output

        




        