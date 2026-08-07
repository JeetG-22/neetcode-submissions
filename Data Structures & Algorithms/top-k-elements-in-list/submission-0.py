class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        sort = sorted(counts.items(), key=lambda item: item[1])
        output = []
        for i in range(k):
            output.append(sort[-1 - i][0])
        return output

        