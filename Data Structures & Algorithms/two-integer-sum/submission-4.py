class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            desire = target - nums[i]
            if desire in map:
                return [map[desire], i]
            map[nums[i]] = i