class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_val = nums[0]
        while l < r:
            if nums[l] < nums[r]:
                r -= 1
                min_val = min(min_val, nums[l])
            else:
                l += 1
                min_val = min(min_val, nums[r])

        return min_val