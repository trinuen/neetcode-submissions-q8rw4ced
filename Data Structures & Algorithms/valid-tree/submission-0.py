class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        q = deque([(0, 0)])
        adj_list = {i:[] for i in range(n)}
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
        
        while q:
            node, prev = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for end in adj_list[node]:
                if end not in visited:
                    q.append((end, node))
            adj_list[node] = []
        return len(visited) == n