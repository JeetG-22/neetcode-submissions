class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            max_ind = i + 1
            for j in range(max_ind + 1, len(arr)):
                if arr[max_ind] < arr[j]:
                    max_ind = j
            arr[i] = arr[max_ind]
        arr[-1] = -1
        return arr


        