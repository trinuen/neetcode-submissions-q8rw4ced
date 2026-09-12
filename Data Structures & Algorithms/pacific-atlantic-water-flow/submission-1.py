class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pac_visit = set()
        atl_visit = set()
        pac = deque([])
        atl = deque([])
        for j in range(COLS):
            pac.append((0, j))
            atl.append((ROWS-1, j))
            pac_visit.add((0, j))
            atl_visit.add((ROWS-1, j))
        
        for i in range(ROWS):
            pac.append((i, 0))
            atl.append((i, COLS-1))
            pac_visit.add((i, 0))
            atl_visit.add((i, COLS-1))

        def add_point(r, c, visit, prev_val, q):
            if ((r, c) in visit  or r < 0 or c < 0 or r >= 
            ROWS or c >= COLS or heights[r][c] < prev_val):
                return
            q.append((r, c))
            visit.add((r, c))
        while pac:
            for _ in range(len(pac)):
                r, c = pac.popleft()
                add_point(r + 1, c, pac_visit, heights[r][c], pac)
                add_point(r, c + 1, pac_visit, heights[r][c], pac)
                add_point(r - 1, c, pac_visit, heights[r][c], pac)
                add_point(r, c - 1, pac_visit, heights[r][c], pac)
        while atl:
            for _ in range(len(atl)):
                r, c = atl.popleft()
                add_point(r + 1, c, atl_visit, heights[r][c], atl)
                add_point(r, c + 1, atl_visit, heights[r][c], atl)
                add_point(r - 1, c, atl_visit, heights[r][c], atl)
                add_point(r, c - 1, atl_visit, heights[r][c], atl)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac_visit and (r, c) in atl_visit:
                    res.append([r, c])
        return res