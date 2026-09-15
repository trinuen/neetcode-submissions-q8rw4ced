class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        took = set()
        res = []
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crs in took:
                return True
            visited.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            res.append(crs)
            took.add(crs)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return res