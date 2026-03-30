class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i in range(len(nums)):
            if target - nums[i] in num:
                return [min(i, num[target - nums[i]]), max(i, num[target - nums[i]])]
            num[nums[i]] = i