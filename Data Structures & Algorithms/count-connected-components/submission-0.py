class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited, seen = set(), set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for c in adj[node]:
                if c in visited:
                    continue
                dfs(c)

        res = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
            if len(visited) == n:
                return res