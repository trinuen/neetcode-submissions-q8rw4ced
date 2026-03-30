class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i in range(len(nums)):
            if target - nums[i] in num:
                res = [i, num[target - nums[i]]]
                break
            num[nums[i]] = i
        return sorted(res)