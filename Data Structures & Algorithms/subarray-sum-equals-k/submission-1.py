class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre_sum = {0: 1}
        pre = 0

        for num in nums:
            total = num + pre
            target = total - k
            if target in pre_sum:
                res += pre_sum[target]
            pre_sum[total] = pre_sum.get(total, 0) + 1
            pre = total
        return res
