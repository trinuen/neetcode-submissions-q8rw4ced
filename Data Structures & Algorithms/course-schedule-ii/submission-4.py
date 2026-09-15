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
            if adj_list[crs] == []:
                if crs not in took:
                    res.append(crs)
                    took.add(crs)
                return True
            visited.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre): return False
            adj_list[crs] = []
            if crs not in took:
                res.append(crs)
                took.add(crs)
            visited.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return list(res)