class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def count(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = count(n-1) + count(n-2)
            return cache[n]

        return count(n)
        