class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        def memo(r, c, cache):
            if r == ROW or c == COL or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROW - 1 and c == COL - 1:
                return 1
            cache[r][c] = memo(r + 1, c, cache) + memo(r, c+1, cache)
            return cache[r][c]
        table = [[0] * COL for i in range(ROW)]
        return memo(0,0,table)

        