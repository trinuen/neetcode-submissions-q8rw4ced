class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i: set() for i in range(1, len(edges)+1)}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        visited = set()
        def dfs(u, v):
            if u == v:
                return True
            visited.add(u)
            for s in adj[u]:
                if s in visited:
                    continue
                if dfs(s, v):
                    visited.remove(u)
                    return True
            visited.remove(u)
            return False
        res = [-1, -1]
        for p, c in edges:
            adj[p].remove(c)
            adj[c].remove(p)
            if dfs(p, c):
                res = [p, c]
            adj[p].add(c)
            adj[c].add(p)
        return res
        