class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        visit = [[False for _ in range(COLS)] for _ in range(ROWS)]

        q = deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        while q:
            r, c = q.popleft()
            for dx, dy in directions:
                new_r = r + dx
                new_c = c + dy
                if (0 <= new_r < ROWS and 
                0 <= new_c < COLS and
                not visit[new_r][new_c] and
                grid[new_r][new_c] == INF):
                    grid[new_r][new_c] = grid[r][c] + 1
                    visit[new_r][new_c] = True
                    q.append([new_r, new_c])




