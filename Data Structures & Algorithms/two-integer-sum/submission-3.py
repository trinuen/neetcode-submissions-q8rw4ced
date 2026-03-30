class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_count = {}

        for i, j in enumerate(nums):
            if (target - j) in num_count:
                return [num_count[target-j], i]
            num_count[j] = i
