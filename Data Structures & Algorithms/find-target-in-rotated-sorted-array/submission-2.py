class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #[3,4,5,6,1,2] target=1
        #       ^
        #[3,4,-1,0,1,2]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(nums[m])

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else: #nums[m] < nums[l]
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1