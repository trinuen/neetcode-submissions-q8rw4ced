class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * (n) for _ in range(m)]
        print(memo)
        def dfs(x, y):
            if x >= m or y >= n:
                return 0
            if memo[x][y] != -1:
                return memo[x][y]
    
            if x == m-1 and y == n-1:
                return 1

            total = dfs(x + 1, y) + dfs(x, y + 1)
            memo[x][y] = total
            return total

        return dfs(0, 0)
