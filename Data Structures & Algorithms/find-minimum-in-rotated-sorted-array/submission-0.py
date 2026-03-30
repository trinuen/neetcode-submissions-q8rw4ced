class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7,8,9,1,2,3]
        #[2,1]
        min_num = float('inf')

        #if last_element > first_element: normal binary search
        if nums[-1] >= nums[0]:
            return nums[0]

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



