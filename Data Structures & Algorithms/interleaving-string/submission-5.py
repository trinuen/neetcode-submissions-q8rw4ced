class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #abdcd
        #cdab
        #abcdacdb
        memo = {}
        def dfs(i, j):
            if i + j == len(s3):
                return (i == len(s1)) and (j == len(s2))
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] =  False
            if i < len(s1) and s1[i] == s3[i + j]:
                memo[(i, j)] = dfs(i+1, j)

            if not memo[(i, j)] and j < len(s2) and s2[j] == s3[i + j]:
                memo[(i, j)] =  dfs(i, j+1)

            return memo[(i, j)]

        return dfs(0, 0)