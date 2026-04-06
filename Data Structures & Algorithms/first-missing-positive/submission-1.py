class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #[3,1,0]
        #[-3,1,-4]
        #
        #[1,2,4]
        #[-1,-2,4]
        #
        #[1,2,4,5,6,3,1]
        #[-1,-2,-4,-5,-6,-3,1]
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if idx >= 0 and idx < len(nums):
                if nums[idx] < 0:
                    continue
                elif nums[idx] == 0:
                    nums[idx] = -(len(nums) + 1)
                else:
                    nums[idx] = -nums[idx]
        res = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                res += 1
            else:
                return res
        return res