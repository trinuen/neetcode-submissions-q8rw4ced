class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {len(nums): 0}
        def dfs(curr_idx, prev_idx):
            if curr_idx == len(nums):
                return 0

            if (curr_idx,prev_idx) in memo:
                return memo[(curr_idx,prev_idx)]

            LIS = dfs(curr_idx+1, prev_idx)
            
            if prev_idx == -1 or nums[prev_idx] < nums[curr_idx]:
                LIS = max(LIS, 1+dfs(curr_idx+1, curr_idx))

            if curr_idx not in memo:
                memo[(curr_idx, prev_idx)] = LIS
            return LIS
        
        return dfs(0, -1)
