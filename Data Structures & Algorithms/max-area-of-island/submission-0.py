class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        area = 0
        def dfs(i, j):
            if (i >= ROWS or i < 0 or j >= COLS or j < 0 or grid[i][j] == 0):
                return 0
            grid[i][j] = 0
            return dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1) + 1

        for i in range(ROWS):
            for j in range(COLS):
                area = max(dfs(i, j), area)
        
        return area