class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(idx, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return
            for j in range(idx, len(nums)):
                if total + nums[j] > target:
                    return
                curr_list.append(nums[j])
                dfs(j, curr_list, total + nums[j])
                curr_list.pop()

        dfs(0, [], 0)
        return res
