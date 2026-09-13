class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        not_surrounded = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == 'X' 
            or (r, c) in not_surrounded):
                return
            not_surrounded.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][COLS-1] == 'O':
                dfs(i, COLS-1)
        
        for j in range(COLS):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[ROWS-1][j] == 'O':
                dfs(ROWS-1, j)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in not_surrounded and board[r][c] == 'O':
                    board[r][c] = 'X'