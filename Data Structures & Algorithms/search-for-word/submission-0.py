class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        def dfs(i, j, length):
            if length == len(word):
                return True
            if (i < 0 
                or i >= ROWS 
                or j < 0 or j >= COLS 
                or word[length] != board[i][j]
                or (i,j) in path):
                return False
            path.add((i,j))
            res = (dfs(i+1, j, length + 1) 
                or dfs(i-1, j, length + 1) 
                or dfs(i, j+1, length + 1) 
                or dfs(i, j-1, length + 1))
            path.remove((i,j))
            return res
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0): return True
        return False