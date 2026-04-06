class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #[8,1,0]
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
                if nums[idx] == 0:
                    nums[idx] = -(len(nums) + 1)
                elif nums[idx] > 0:
                    nums[idx] = -nums[idx]
    
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums) + 1