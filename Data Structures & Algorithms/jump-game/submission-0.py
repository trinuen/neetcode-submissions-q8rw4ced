class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jump = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= can_jump:
                can_jump = i
        
        return True if can_jump == 0 else False