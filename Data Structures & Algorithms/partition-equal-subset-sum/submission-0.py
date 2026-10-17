class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i, curr, total):
            if (curr, i) in cache:
                return cache[(curr, i)]
            if total == 2*curr:
                cache[(curr, i)] = True
                return True
            if i >= len(nums) or curr > total:
                return False

            if dfs(i+1, curr+nums[i], total) or dfs(i+1, curr, total):
                return True
            
            cache[(curr, i)] = False
            return False

        return dfs(0, 0, sum(nums))