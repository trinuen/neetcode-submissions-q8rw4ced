class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {0: 1}
        pre = 0

        for num in nums:
            total = num + pre
            target = total - k
            if target in prefixSum:
                res += prefixSum[target]
            prefixSum[total] = prefixSum.get(total, 0) + 1
            pre = total
        return res