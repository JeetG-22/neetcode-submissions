class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if ans[i] < arr[j]:
                    ans[i] = arr[j] 
        ans[-1] = -1
        return ans
        