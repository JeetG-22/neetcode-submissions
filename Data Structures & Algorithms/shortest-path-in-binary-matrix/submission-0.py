class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)
    
    def bfs(self, grid):
        if grid[0][0] == 1:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        length = 1
        q = deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                neighbors = [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for rd, cd in neighbors:
                    row = r + rd
                    col = c + cd
                    if min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == 1:
                        continue
                    q.append((row,col))
                    visited.add((row,col))
            length += 1
        return -1
        