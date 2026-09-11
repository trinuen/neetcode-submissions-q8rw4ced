class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        fresh = set()
        q = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])

        def addPoint(r, c):
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            q.append((r, c))
            visited.add((r, c))
            fresh.remove((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
    
        if not fresh: return 0

        time = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addPoint(r + 1, c)
                addPoint(r, c + 1)
                addPoint(r - 1, c)
                addPoint(r, c - 1)
            time += 1
        
        return time if not fresh else -1
                
        
