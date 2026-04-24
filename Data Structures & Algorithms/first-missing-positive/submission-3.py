class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #smallest possible sol is 1
        #largest possible sol is n+1 where n=len(nums)

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if idx >= 0 and idx < len(nums):
                if nums[idx] == 0:
                    nums[idx] = -(nums[i])
                elif nums[idx] > 0:
                    nums[idx] = -nums[idx]
    
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums) + 1