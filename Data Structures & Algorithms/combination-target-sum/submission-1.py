class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return
            if idx >= len(nums) or total > target:
                return
            curr_list.append(nums[idx])
            dfs(idx, curr_list, total + nums[idx])
            curr_list.pop()
            dfs(idx+1, curr_list, total)

        dfs(0, [], 0)
        return res
