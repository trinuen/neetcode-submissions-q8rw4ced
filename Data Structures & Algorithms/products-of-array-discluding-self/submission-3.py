class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #[1,1,2,8]
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        suf = 1
        for i in range(len(nums)-2, -1, -1):
            suf *= nums[i+1]
            res[i] *= suf

        return res