class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # j = 0
        cur_sum = 0
        res = nums[0]
        for i in range(len(nums)):
            cur_sum += nums[i]
            res = max(res, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
                # j += 1
        return res