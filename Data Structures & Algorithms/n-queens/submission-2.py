from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag1 = set()
        diag2 = set()
        res = []
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if (c in col or 
                (r+c) in diag1 or 
                (r-c) in diag2):
                    continue
                
                col.add(c)
                diag1.add(r+c)
                diag2.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                col.remove(c)
                diag1.remove(r+c)
                diag2.remove(r-c)
                board[r][c] = "."

        
        dfs(0)
        return res