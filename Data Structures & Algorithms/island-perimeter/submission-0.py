class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        res = [0]
        directions = [[1, 0], [-1,0], [0,1], [0,-1]]
        def dfs(i, j):
            perimeter = 4
            for x, y in directions:
                new_i = i + x
                new_j = j + y
                if new_i >= ROWS or new_i < 0 or new_j >= COLS or new_j < 0 or grid[new_i][new_j] == 0:
                    continue
                if grid[new_i][new_j] == 1:
                    perimeter -= 1
            res[0] += perimeter
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
        return res[0]