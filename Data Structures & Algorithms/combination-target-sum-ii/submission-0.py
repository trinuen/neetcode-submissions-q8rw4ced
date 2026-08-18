class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(curr_list, i, total):
            if total == target:
                res.append(curr_list.copy())
                return
            if (i >= len(candidates) or total > target):
                return
            curr_list.append(candidates[i])
            dfs(curr_list, i + 1, total + candidates[i])
            curr_list.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(curr_list, i + 1, total)
        dfs([], 0, 0)
        return res