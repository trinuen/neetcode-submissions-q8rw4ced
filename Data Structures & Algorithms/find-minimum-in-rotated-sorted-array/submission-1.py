class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = float('inf')

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                min_num = min(min_num, nums[mid])
                r = mid - 1

        return min_num